## Overview

This Python script scrapes stock data from Yahoo Finance for a ticker symbol, eg AAPL. The website is "https://finance.yahoo.com/quote/AAPL/", where the last 4 symbols indicate the ticker symbol. This is inputted by the user in the script. 

## Prerequisites

- Python 3.12.0
- Required Python packages: `requests`, `beautifulsoup4`, `csv`, `datetime`

Install the required packages using:

```bash
pip install requests beautifulsoup4

## Overview

Scrapes stock data from Yahoo Finance for a user inputted ticker symbol, eg AAPL.

## Prerequisites

- Python 3.12.0
- Required Python packages: `requests`, `beautifulsoup4`, `csv`, `datetime`

Install the required packages using:

```bash
pip install requests beautifulsoup4
```

## Important Note

Ensure compliance with Yahoo's terms of service and policies. Web scraping may be subject to legal and ethical considerations.

## Customization

Feel free to customize the script to meet your specific needs. Possible improvements include adding error handling, adjusting the time delay, or enhancing the user interface.


### 1. Get User Input

The script prompts the user to enter the name of the ticker they are interested in getting information for

```python
symbol = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
```

### 2. Save to CSV File

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
