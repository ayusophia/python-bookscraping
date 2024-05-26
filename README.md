Python Script for Scraping Book Details

This Python script scrapes book details from the e-commerce website http://books.toscrape.com/. It extracts title, price, and rating information for books listed on the first three pages of the website.

Features:
Error Handling: Includes exception handling for potential requests library errors and attribute errors during parsing.
Respectful Scraping: Implements a one-second delay between requests to avoid overwhelming the website's server.
Data Organization: Saves the scraped data as a well-formatted CSV file named books12.csv.

Requirements:
Python 3 (tested with 3.x)
requests library (pip install requests)
beautifulsoup4 library (pip install beautifulsoup4)
pandas library (pip install pandas)

Usage:
Clone or download this repository to your local machine.
Install the required libraries (pip install requests beautifulsoup4 pandas).
Run the script from your terminal using python book_scraper.py (replace book_scraper.py with the actual filename if different).

Output:
The script will print a confirmation message upon successful scraping and saving the data as books12.csv.
