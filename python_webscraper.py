import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_yahoo_finance(symbol):
    """
    Scrapes stock data from Yahoo Finance for a user inputted ticker symbol, eg AAPL.
    """
    url = f"https://finance.yahoo.com/quote/{symbol}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the selectors (Yahoo Finance changes these frequently - so check again if it changes)
        name = soup.find('title')
        price = soup.find('span', class_= "base    yf-ipw1h0") or soup.find('span', class_="price yf-15b2o7n")
        # change = soup.find('span', class_="base  txt-positive  yf-ipw1h0", attrs={'data-testid': 'qsp-price-change-percent'})
        change = soup.find('span', attrs={'data-testid': 'qsp-price-change-percent'})
        
        if not (name and price and change):
            print("Error: Could not find required data. Yahoo's HTML structure may have changed.")
            return None
        
        stock_data = {
            'symbol': symbol,
            'name': name.text.strip(),
            'price': price.text.strip(),
            'change': change.text.strip(),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Get additional data
        data_table = soup.find('div', class_='D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i)')
        if data_table:
            rows = data_table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                if len(cols) == 2:
                    key = cols[0].text.strip()
                    value = cols[1].text.strip()
                    stock_data[key] = value
        
        return stock_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

# Change to your directory if preferred
def save_to_csv(data, filename="stock_data.csv"):
    """Saves scraped data to a CSV file."""
    if not data:
        return
        
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

if __name__ == "__main__":
    symbol = input("Enter stock symbol (e.g., AAPL): ").strip().upper() # Convert to upper case
    stock_data = scrape_yahoo_finance(symbol)
    
    if stock_data:
        print("\nScraped Stock Data:")
        for key, value in stock_data.items():
            print(f"{key}: {value}")
        
        save_to_csv(stock_data)
        print(f"\nData saved to stock_data.csv")
    else:
        print("Failed to scrape data.")
