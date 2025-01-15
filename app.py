import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Market Share Analysis", layout="wide")

def load_data(uploaded_file):
    """Load data from an uploaded file."""
    try:
        if uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            st.error("Unsupported file format. Please upload a .csv or .xlsx file.")
            return None
        return df
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None

def calculate_market_share(all_sales_df, our_sales_df, date_col, sales_col):
    """Calculate market share by date."""
    # Group by date and sum sales
    all_sales_grouped = all_sales_df.groupby(date_col)[sales_col].sum().reset_index()
    our_sales_grouped = our_sales_df.groupby(date_col)[sales_col].sum().reset_index()
    
    # Merge the dataframes
    market_share = pd.merge(
        all_sales_grouped,
        our_sales_grouped,
        on=date_col,
        how='inner',
        suffixes=('_total', '_our')
    )
    
    # Calculate market share percentage
    market_share['market_share_pct'] = (market_share[f'{sales_col}_our'] / market_share[f'{sales_col}_total'] * 100).round(2)
    
    return market_share

def main():
    st.title("Market Share Analysis App")
    
    # File uploaders
    st.sidebar.header("Upload Data")
    all_sales_file = st.sidebar.file_uploader("Upload All Sales Data (CSV or Excel)", type=["csv", "xlsx"])
    our_sales_file = st.sidebar.file_uploader("Upload Our Sales Data (CSV or Excel)", type=["csv", "xlsx"])
    
    if all_sales_file and our_sales_file:
        # Load data
        all_sales_df = load_data(all_sales_file)
        our_sales_df = load_data(our_sales_file)
        
        if all_sales_df is not None and our_sales_df is not None:
            # Allow user to select date and sales columns
            st.sidebar.header("Select Columns")
            date_col = st.sidebar.selectbox(
                "Select Date Column",
                options=all_sales_df.columns,
                index=0
            )
            sales_col = st.sidebar.selectbox(
                "Select Sales Column",
                options=all_sales_df.columns,
                index=1
            )
            
            # Filter data based on selected columns
            try:
                all_sales_df[date_col] = pd.to_datetime(all_sales_df[date_col], errors='coerce')
                our_sales_df[date_col] = pd.to_datetime(our_sales_df[date_col], errors='coerce')
                
                # Drop rows with invalid dates
                all_sales_df = all_sales_df.dropna(subset=[date_col])
                our_sales_df = our_sales_df.dropna(subset=[date_col])
                
                # Calculate market share
                market_share_df = calculate_market_share(all_sales_df, our_sales_df, date_col, sales_col)
                
                if market_share_df.empty:
                    st.error("No matching data found between the two files. Please check the selected columns.")
                    return
                
                # Add total metrics at the top
                total_all_sales = market_share_df[f'{sales_col}_total'].sum()
                total_our_sales = market_share_df[f'{sales_col}_our'].sum()
                overall_market_share = (total_our_sales / total_all_sales * 100).round(2)
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Total All Sales", f"{total_all_sales:,}")
                col2.metric("Total Our Sales", f"{total_our_sales:,}")
                col3.metric("Overall Market Share", f"{overall_market_share}%")
                
                # Date range filter
                st.sidebar.header("Filters")
                min_date = market_share_df[date_col].min().to_pydatetime().date()
                max_date = market_share_df[date_col].max().to_pydatetime().date()
                
                date_range = st.sidebar.date_input(
                    "Select Date Range",
                    value=(min_date, max_date),
                    min_value=min_date,
                    max_value=max_date
                )
                
                # Filter data based on date range
                filtered_df = market_share_df[
                    (market_share_df[date_col].dt.date >= date_range[0]) &
                    (market_share_df[date_col].dt.date <= date_range[1])
                ]
                
                if filtered_df.empty:
                    st.warning("No data available for the selected date range.")
                    return
                
                # Create visualizations
                st.header("Market Share Analysis")
                
                # Time series chart for market share
                st.subheader("Market Share Over Time")
                fig_market_share = px.line(
                    filtered_df,
                    x=date_col,
                    y='market_share_pct',
                    title="Market Share % Over Time"
                )
                fig_market_share.update_layout(
                    yaxis_title="Market Share %",
                    hovermode='x unified'
                )
                st.plotly_chart(fig_market_share, use_container_width=True)
                
                # Bar chart for sales comparison
                st.subheader("Sales Comparison Over Time")
                fig_sales = go.Figure()
                fig_sales.add_trace(go.Bar(
                    x=filtered_df[date_col],
                    y=filtered_df[f'{sales_col}_total'],
                    name='All Sales',
                    marker_color='rgb(55, 83, 109)'
                ))
                fig_sales.add_trace(go.Bar(
                    x=filtered_df[date_col],
                    y=filtered_df[f'{sales_col}_our'],
                    name='Our Sales',
                    marker_color='rgb(26, 118, 255)'
                ))
                fig_sales.update_layout(
                    title='All Sales vs Our Sales',
                    barmode='group',
                    hovermode='x unified'
                )
                st.plotly_chart(fig_sales, use_container_width=True)
                
                # Display raw data
                st.subheader("Raw Data")
                st.dataframe(filtered_df)
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.exception(e)
        else:
            st.error("Failed to load one or both files. Please check the file formats.")
    else:
        st.info("Please upload both 'All Sales' and 'Our Sales' files to begin.")

if __name__ == "__main__":
    main()
