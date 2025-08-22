# 📰 Simple Web Scraper for News Headlines

A beginner-friendly Python project to fetch and display news headlines from online news websites.  
This project demonstrates **web scraping**, **HTML parsing**, and **clean documentation** practices.

---

## ✨ Features

- Fetch web page content using `requests`.
- Parse HTML for headline elements (`<h2>`, `<h3>`).
- Display headlines in a clean, numbered list.
- Error handling for invalid URLs or failed requests.
- (Optional) Export results to a file.

## 🛠️ Tech Stack

- **Python 3.x**
- [Requests](https://docs.python-requests.org/en/master/) – for HTTP requests
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) – for HTML parsing

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/kishorongit/simple-news-scraper.git
cd simple-news-scraper
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
Or manually:
```bash
pip install requests beautifulsoup4
```

### 3. Run the Scraper

```bash
python scraper.py
```

### 📌 Example Output

```text
🌐 Fetching headlines from: https://www.bbc.com/news

📰 Latest Headlines:

1. 'My youngest child doesn't know what fruit tastes like': Gaza residents on famine
2. India top court shelves plan to lock up Delhi's one million street dogs
3. US to review all 55 million visas to check if holders broke rules
4. Global postal services halt US deliveries over tariffs
5. Giant octopus steals camera for a selfie
6. New Jersey under state of emergency for Hurricane Erin
7. Computer science graduates struggle to secure their first jobs
8. Beijing opposes 'bully' US for 50% tariffs on India
9. New dinosaur species named after world record sailor
...
```

## 🔮 Future Enhancements

- Support multiple websites
- Export results to CSV or JSON
- Add command-line arguments (choose site, output format)
- Add automated tests

## 📄 License

This project is licensed under the MIT License. Please read more at: [Exploring the MIT Open Source License: A 
Comprehensive Guide](https://test-mit-tlo.pantheonsite.io/understand-ip/exploring-mit-open-source-license-comprehensive-guide)

## 👤 Author

Your Name – [subedi-kishor](https://www.linkedin.com/in/subedi-kishor/)

GitHub: [kishorongit](https://github.com/kishorongit)

## ⚠️ Disclaimer

This project is for **educational purposes only**.</br>
Web scraping may violate the Terms of Service of some websites.</br>
Always check site policies before scraping.