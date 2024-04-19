import yfinance as yf
from datetime import datetime, timedelta
    
# Get the current date
current_date = datetime.today()

# Calculate the date one year ago
one_year_ago = current_date - timedelta(days=365)

st = "SWSOLAR"
# Define the ticker symbol
ticker_symbol = st+".NS"

# Fetch historical data for the stock
stock_data = yf.download(ticker_symbol, start=one_year_ago, end=current_date)

# Reset index to make 'Date' a column
stock_data.reset_index(inplace=True)

stock_data['Stock'] = st

# Extract required columns
stock_data = stock_data[['Stock', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

# Rename 'Adj Close' to 'Close' for consistency
stock_data.rename(columns={'Adj Close': 'Close'}, inplace=True)

# Check if 'Dividends' column exists before attempting to access it
if 'Dividends' in stock_data.columns:
    stock_data = stock_data[['Stock', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close', 'Dividends']]
else:
    print("Dividends data not available for the specified stock.")

# Extract year and month from the 'Date' column
stock_data['Day'] = stock_data['Date'].dt.day
stock_data['Month'] = stock_data['Date'].dt.month
stock_data['Year'] = stock_data['Date'].dt.year

# Fetching information about the ticker
ticker = yf.Ticker(st + ".NS")
ticker_info = ticker.info

# Extracting specific data from ticker_info
data_to_extract = {
    'Country': ticker_info.get('country', None),
    'Website': ticker_info.get('website', None),
    'Industry': ticker_info.get('industry', None),
    'Sector': ticker_info.get('sector', None),
    'Long Business Summary': ticker_info.get('longBusinessSummary', None),
    'Payout Ratio': ticker_info.get('payoutRatio', None),
    'Profit Margins': ticker_info.get('profitMargins', None),
    'Earnings Quarterly Growth': ticker_info.get('earningsQuarterlyGrowth', None),
    'Exchange': ticker_info.get('exchange', None),
    'Long Name': ticker_info.get('longName', None),
    'Time Zone Short Name': ticker_info.get('timeZoneShortName', None),
    'Target High Price': ticker_info.get('targetHighPrice', None),
    'Target Low Price': ticker_info.get('targetLowPrice', None),
    'Target Mean Price': ticker_info.get('targetMeanPrice', None),
    'Target Median Price': ticker_info.get('targetMedianPrice', None),
    'Total Cash': ticker_info.get('totalCash', None),
    'Total Cash Per Share': ticker_info.get('totalCashPerShare', None),
    'EBITA': ticker_info.get('ebita', None),
    'Total Debt': ticker_info.get('totalDebt', None),
    'Total Revenue': ticker_info.get('totalRevenue', None),
    'Debt To Equity': ticker_info.get('debtToEquity', None),
    'Revenue Per Share': ticker_info.get('revenuePerShare', None),
    'Earnings Growth': ticker_info.get('earningsGrowth', None),
    'Revenue Growth': ticker_info.get('revenueGrowth', None),
    'Gross Margins': ticker_info.get('grossMargins', None),
    'EBITA Margins': ticker_info.get('ebitdaMargins', None),
    'Operating Margins': ticker_info.get('operatingMargins', None)
}

# Convert the dictionary to a DataFrame
ticker_info_df = pd.DataFrame([data_to_extract])

# Display the DataFrame
print(ticker_info_df)
# Display the data
print(stock_data)

