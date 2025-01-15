# Market Share Analysis App

This is a Streamlit app designed to analyze market share by comparing two datasets: one for all sales and one for our sales. The app calculates market share as the percentage of our sales compared to total sales and provides interactive visualizations and filters for deeper analysis.

## Features

- **Data Loading**: Loads two Excel files (`all_sales.xlsx` and `our_sales.xlsx`) containing sales data.
- **Market Share Calculation**: Computes market share as the percentage of our sales relative to total sales.
- **Interactive Filters**: Allows users to filter data by date range and other optional columns (e.g., product category).
- **Visualizations**:
  - Time series charts for market share trends and sales volumes.
  - Bar charts comparing monthly all sales vs. our sales.
- **Performance Metrics**: Displays key metrics such as total sales, average market share, and more.

## Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.8 or higher
- Streamlit
- Pandas
- Plotly
- Openpyxl (for reading Excel files)

You can install the required Python packages using the following command:

```bash
pip install streamlit pandas plotly openpyxl
