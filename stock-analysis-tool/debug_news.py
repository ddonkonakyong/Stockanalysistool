import yfinance as yf
import json

def check_news(ticker):
    print(f"--- Checking News for {ticker} ---")
    try:
        stock = yf.Ticker(ticker)
        news = stock.news
        print(f"News count: {len(news)}")
        if news:
            print(json.dumps(news[0], indent=2))
        else:
            print("No news found via .news attribute.")
            
    except Exception as e:
        print(f"Error: {e}")

check_news("000660.KS")
check_news("AAPL") # Control check
