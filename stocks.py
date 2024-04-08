import requests

#API_KEY = 'ZEED7DRC6K2G5U8Z' # for intraday

API_KEY = '6AVIIWDPD01ONZPA' # for daily

# List of stocks you're interested in
# stocks = ['HDFCBANK', 'SBIN', 'CANBK', 'IDFCFIRSTB']
stocks = ['SBIN', 'HDFCBANK']

# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stocks}.BSE&apikey={API_KEY}'
# r = requests.get(url)
# data = r.json()

# print(data)

for stock in stocks:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}.BSE&apikey={API_KEY}'
    # url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stocks}.BSE&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()
    
    # Process data here, for example:
    # Extract relevant information and store it in a database or file
    # Print data for demonstration purposes
    print(f"Data for {stock}:")
    print(data)
    print("--------------------------")