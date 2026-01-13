import yfinance as yf

 
tickers = [
    "AAPL", "GOOGL", "MSFT", "AMZN",
    "META", "NVDA", "NFLX", "BMW.DE",
    "MBG.DE","F","VOW3.DE","LMT","NOC", 
    "BTC-USD","TTWO"
]

 
for t in tickers:
    stock = yf.Ticker(t)
    info = stock.info
    current_price = stock.history(period="1d")["Close"][0]

    print("----------------------------")
    print("Ticker:", t)
    print("Name:", info.get("longName", "N/A"))
    print("Website:", info.get("website", "N/A"))
    print("Current Price:", current_price)

print("----------------------------")
 
 
user_ticker = input("Enter a ticker symbol to look up: ")

stock = yf.Ticker(user_ticker)
info = stock.info
current_price = stock.history(period="1d")["Close"][0]

print("----------------------------")
print("Name:", info.get("longName", "N/A"))
print("Website:", info.get("website", "N/A"))
print(f"{user_ticker} Current Price:", current_price)
 