# Yahoo Python Webscraper

## Overview

This Python script scrapes stock data from Yahoo Finance for a ticker symbol, eg AAPL. The website is "https://finance.yahoo.com/quote/AAPL/", where the last 4 symbols indicate the ticker symbol. This is inputted by the user in the script. 

**Example Tickers:**  
Apple Inc.: AAPL  
Microsoft Corporation: MSFT  
Amazon.com, Inc.: AMZN  
Meta (formerly Facebook) Inc.: META  
Alphabet Inc. (Google): GOOGL  
Tesla Motors: TSLA  
The Goldman Sachs Group, Inc.: GS  
Coca-Cola Company: KO  
International Business Machines: IBM  
Netflix Inc.: NFLX  

## Prerequisites

- Python 3.12.0
- Required Python packages: `requests`, `beautifulsoup4`, `csv`, `datetime`

Install the required packages using:

```bash
pip install requests beautifulsoup4

## Overview

Scrapes stock data from Yahoo Finance using a user-inputted ticker symbol, eg, AAPL.

## Prerequisites

- Python 3.12.0
- Required Python packages: `requests`, `beautifulsoup4`, `csv`, `datetime`

Install the required packages using:

```bash
pip install requests beautifulsoup4
```

### 1. Get User Input

The script prompts the user to enter the name of the ticker they are interested in getting information for

```python
symbol = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
```

### 2. Outputs

The script currently outputs symbol, name, price, percent change, and the timestamp at which it was requested.  

Example Output:  
```python
Scraped Stock Data:  
symbol: VOO  
name: Vanguard S&P 500 ETF (VOO) Stock Price, News, Quote & History - Yahoo Finance  
price: 554.39  
change: +(0.57%)  
timestamp: 2025-06-11 13:34:36

```

### 3. Save to CSV File

The save_to_csv function saves the information to a CSV file. To specify the directory, you can change the filename. 

```python
def save_to_csv(data, filename="stock_data.csv"):
    """Saves scraped data to a CSV file."""
    if not data:
        return
        
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)
```

## Important Note

Ensure compliance with Yahoo's terms of service and policies. Web scraping may be subject to legal and ethical considerations.

## Customization

Possible improvements include appending requests to the same CSV file, adding better error handling, adjusting the time delay, and enhancing the user interface.



