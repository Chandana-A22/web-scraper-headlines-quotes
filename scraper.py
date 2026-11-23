import requests
from bs4 import BeautifulSoup
import json
import time

base_url = "https://quotes.toscrape.com/"
all_quotes = []

for page in range(1, 11):
    url = f"{base_url}page/{page}/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text")
            author = quote.find("small", class_="author")
            tags = quote.find_all("a", class_="tag")

            if text and author:
                all_quotes.append({
                    "quote": text.get_text(strip=True),
                    "author": author.get_text(strip=True),
                    "tags": [tag.get_text(strip=True) for tag in tags]
                })

        print(f"Page {page} scraped successfully!")

        time.sleep(1)  # Be polite to the website

    except requests.exceptions.RequestException as e:
        print(f"Error on page {page}: {e}")

with open("quotes.json", "w", encoding="utf-8") as file:
    json.dump(all_quotes, file, indent=4, ensure_ascii=False)

print(f"\nTotal quotes saved: {len(all_quotes)}")
print("Data saved in quotes.json")