import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the e-commerce website
url = 'http://books.toscrape.com/'

# Function to extract book details
def get_book_details(book_url):
    try:
        response = requests.get(book_url)
        response.raise_for_status()  # Ensure we notice bad responses
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').text
        price = soup.find('p', class_='price_color').text
        rating = soup.find('p', class_='star-rating')['class'][1]
        return {
            'Title': title,
            'Price': price,
            'Rating': rating
        }
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except AttributeError as e:
        print(f"Parsing failed: {e}")
        return None

# List to store book details
book_list = []

# Loop through the first few pages (for simplicity, we limit it to 3 pages)
for page in range(1, 4):
    try:
        response = requests.get(url + f'catalogue/page-{page}.html')
        response.raise_for_status()  # Ensure we notice bad responses
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('h3')
        
        for book in books:
            book_href = book.a['href']
            book_url = url + 'catalogue/' + book_href.replace('../../../', '')
            details = get_book_details(book_url)
            if details:
                book_list.append(details)
        
        time.sleep(1)  # Sleep to avoid getting blocked
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        continue

# Convert to DataFrame
book_df = pd.DataFrame(book_list)

# Save to CSV
book_df.to_csv('books12.csv', index=False)
print("Book details scraped and saved to books.csv")
