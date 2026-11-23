# Web Scraper for Quotes

## Project Overview
This project is a Python web scraper that collects quotes, authors, and tags from a public website and saves them in JSON format.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- JSON

## Features
- Fetches webpage content
- Extracts quotes and author names
- Collects tags
- Scrapes multiple pages
- Saves collected data into `quotes.json`
- Handles HTTP request errors
- Includes a delay between requests

## Data Source
https://quotes.toscrape.com/

Quotes to Scrape is a public practice website designed for learning web scraping.

## How to Run
Install the libraries:

```bash
pip install requests beautifulsoup4
```

Run the scraper:

```bash
python scraper.py
```

The scraped data will be saved in `quotes.json`.

## Output
The JSON file contains quotes, authors, and tags from the website.
