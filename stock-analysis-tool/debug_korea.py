from src.utils import fetch_stock_info
import pandas as pd

def check_korean_stock_fix(ticker):
    print(f"--- Checking {ticker} with UPDATED utils ---")
    info = fetch_stock_info(ticker)
    
    if info:
        print("Final Price:", info.get('currentPrice'))
        print("Final FCF:", info.get('freeCashFlow'))
        print("Final Total Debt:", info.get('totalDebt'))
        print("Final Total Cash:", info.get('totalCash'))
        print("Shares:", info.get('sharesOutstanding'))
    else:
        print("Failed to fetch info.")

check_korean_stock_fix("005930.KS") # Samsung
