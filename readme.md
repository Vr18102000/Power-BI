# Stock Dashboard with Power BI and Python Integration

This repository contains a Power BI dashboard designed for analyzing stock data retrieved using the yfinance library in Python. The dashboard allows users to visualize and analyze stock performance for a variety of symbols.

## Features

- **Dynamic Parameter Selection**: Users can select from 2379 stock symbols through a parameter in the Power BI dashboard.
- **Python Integration**: Upon selecting a stock symbol, users have the option to run a Python script to update the dashboard with the selected stock's data.
- **Automatic Data Refresh**: Once the Python script is executed, all data on the dashboard updates automatically to reflect the selected stock's information.

## Getting Started

To use the dashboard:

1. Clone or download this repository.
2. Open the Power BI file (`Stock.pbix`) using Power BI Desktop.
3. Navigate to the parameter section to select a stock symbol.
4. Upon changing the stock symbol, a prompt will appear to run the Python script.
5. Confirm the execution of the Python script, and the dashboard will update accordingly.

## Requirements

- Power BI Desktop
- Python with yfinance library installed

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
