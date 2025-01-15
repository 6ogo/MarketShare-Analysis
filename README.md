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

## Getting Started
Clone the Repository:

```bash

git clone https://github.com/your-username/market-share-analysis.git
cd market-share-analysis

Prepare Your Data:
Place your sales data in two Excel files:
all_sales.xlsx: Contains all sales data.
our_sales.xlsx: Contains our sales data.

Ensure the files have the required columns:
Offert stängningsdatum: Date of sale.
Tecknande bolag: Region or category (optional).

Antal offerter: Number of conversions/sales.

Run the App:
Start the Streamlit app by running the following command:

bash
Copy
streamlit run app.py
The app will open in your default web browser.

Usage
Upload Data:

Ensure the all_sales.xlsx and our_sales.xlsx files are placed in the Data folder or update the file paths in the code.

Apply Filters:

Use the sidebar to filter data by date range.

If your data includes additional columns (e.g., product category), you can filter by those as well.

Explore Visualizations:

Navigate through the tabs to view time series charts, bar charts, and performance metrics.

Hover over charts to see detailed tooltips.

View Raw Data:

The "Performance Metrics" tab includes a table of raw data for further analysis.

Example Data
Here’s an example of the expected data format for all_sales.xlsx and our_sales.xlsx:

Offert stängningsdatum	Tecknande bolag	Antal offerter
2023-01-01	Region A	100
2023-01-15	Region B	150
2023-02-01	Region A	200
Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Commit your changes.

Submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

