"""
Simple Web Scraper for News Headlines
-------------------------------------
This script fetches news headlines from a given website using requests and BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup


def get_page_content(url: str) -> str:
    """
    Fetch HTML content from the given URL.
    Handles HTTP errors and returns the raw HTML text.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        return response.text
    except requests.RequestException as e:
        print(f" ❌ Error fetching page: {e}")
        return ""


def extract_headlines(html: str) -> list:
    """
    Parse HTML content and extract news headlines.
    Looks for <h2> and <h3> tags (common for headlines).
    Returns a list of headline texts.
    """
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")

    # Collect headlines (site-specific adjustment may be needed)
    headlines = []
    for tag in soup.find_all(["h2", "h3"]):
        text = tag.get_text(strip=True)
        if text and len(text.split()) > 3:  # Filter short/unrelated texts
            headlines.append(text)

    return headlines


def main():
    """
    Main function: runs the scraper step by step.
    """
    url = "https://www.bbc.com/news"  # Example news site
    print(f" 🌐 Fetching headlines from: {url}\n")

    html = get_page_content(url)
    headlines = extract_headlines(html)

    if not headlines:
        print(" ⚠️ No headlines found.")
        return

    print(" 📰 Latest Headlines:\n")
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")


if __name__ == "__main__":
    main()
