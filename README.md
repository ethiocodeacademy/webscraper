# Helloomarket Web Scraper

This is a Python script that allows you to scrape product data from the Helloomarket website and save it to an Excel file. The script uses the following libraries:
- requests
- BeautifulSoup4 (BS4)
- openpyxl

## Installation

To use this script, you need to have Python 3 and the required libraries installed on your machine. You can install them using the following commands:

```
pip install requests
pip install beautifulsoup4
pip install openpyxl
```

## Usage

To use this script, you need to set the `url` variable in the script to the URL of the Helloomarket category page you want to scrape. The script will then extract product data from all pages in that category.

Once you have set the `url` variable, you can run the script using the following command:

```
python scraper.py
```

The script will scrape the product data from the Helloomarket website and save it to an Excel file named `Helloo Market Data.xlsx` in the same directory as the script.
