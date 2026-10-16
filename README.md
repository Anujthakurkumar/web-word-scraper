# 🌐 Web Word Scraper

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3">
  <img src="https://img.shields.io/badge/BeautifulSoup-HTML%20Parsing-2E8B57?style=for-the-badge" alt="BeautifulSoup">
  <img src="https://img.shields.io/badge/Requests-HTTP%20Client-orange?style=for-the-badge" alt="Requests">
  <img src="https://img.shields.io/badge/Project-Micro%20Project-purple?style=for-the-badge" alt="Micro Project">
</p>

<p align="center">
  <b>A lightweight Python tool to extract words from webpages and filter them by character length.</b>
</p>

---

## 🖥️ ASCII Banner

```text
 __        __   _        __        __              _ 
 \ \      / /__| |__     \ \      / /__  _ __ __| |
  \ \ /\ / / _ \ '_ \     \ \ /\ / / _ \| '__/ _` |
   \ V  V /  __/ |_) |     \ V  V / (_) | | | (_| |
    \_/\_/ \___|_.__/       \_/\_/ \___/|_|  \__,_|

          [ WEB WORD SCRAPER v1.0 ]
       --------------------------------
        FETCH  •  EXTRACT  •  FILTER
       --------------------------------
```

## ✨ Features

| Feature | Description |
|---|---|
| 🌍 URL Input | Enter the webpage you want to process |
| 📄 HTML Parsing | Extract webpage text using BeautifulSoup |
| 🔎 Word Extraction | Identify words using regular expressions |
| 📏 Length Filtering | Select words within a minimum and maximum length |
| 💾 File Export | Save extracted words to a `.txt` file |
| ⏱️ Request Timeout | Avoid waiting indefinitely for a response |

## ⚙️ How It Works

```text
       ┌──────────────────────┐
       │     Enter URL        │
       └──────────┬───────────┘
                  ▼
       ┌──────────────────────┐
       │  Fetch Webpage       │
       │  (Requests Library)  │
       └──────────┬───────────┘
                  ▼
       ┌──────────────────────┐
       │  Parse HTML          │
       │  (BeautifulSoup)     │
       └──────────┬───────────┘
                  ▼
       ┌──────────────────────┐
       │  Extract Words       │
       │  (Regular Expression)│
       └──────────┬───────────┘
                  ▼
       ┌──────────────────────┐
       │  Filter by Length    │
       └──────────┬───────────┘
                  ▼
       ┌──────────────────────┐
       │  Save to Text File   │
       └──────────────────────┘
```

## 🧰 Tech Stack

- **Python 3** — core programming language
- **Requests** — sends HTTP requests to retrieve webpage content
- **BeautifulSoup4** — parses HTML
- **Regular Expressions (`re`)** — extracts words using a pattern
- **Sys** — exits the program when the HTTP response is unsuccessful

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/web-word-scraper.git
cd web-word-scraper
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should contain:

```text
requests
beautifulsoup4
```

### 3. Run the script

```bash
python3 web_word_scraper.py
```

## 🎮 Example Run

```text
$ python3 web_word_scraper.py

Enter the URL to scrape: https://example.com
Enter minimum word length: 4
Enter maximum word length: 8
Enter output filename (e.g. output.txt): words.txt

Saved 12 words to words.txt
```

*The number of extracted words depends on the webpage's content.*

## 📂 Project Structure

```text
web-word-scraper/
│
├── web_word_scraper.py   # Main Python script
├── requirements.txt      # Required Python libraries
├── README.md             # Project documentation
└── .gitignore            # Files Git should ignore
```

## 📸 Sample Output

```text
Example
-------
This is a sample webpage for testing.

Filtered words (4–8 characters):
Example
sample
webpage
testing
```

The output file contains one matching word per line.

## 🧠 What I Learned

- Sending HTTP requests using Python
- Working with HTML content
- Extracting text using BeautifulSoup
- Using regular expressions
- Filtering lists with list comprehensions
- Writing results to files

## ⚠️ Limitations

- Processes one webpage per run.
- Does not automatically crawl links to other pages.
- Does not execute JavaScript.
- Extracted content depends on the webpage's HTML and accessibility.

## 🛡️ Responsible Use

Use this tool only on webpages you are permitted to access. Respect website terms of service, `robots.txt` guidance, and applicable request limits. Avoid collecting private or sensitive information.

## 🔮 Future Improvements

- [ ] Add support for processing multiple URLs
- [ ] Add configurable delays between requests
- [ ] Export results to CSV
- [ ] Add duplicate-word removal
- [ ] Add a word-frequency report
- [ ] Build a simple command-line interface with additional options

## 🤝 Contributing

Suggestions and improvements are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## 📜 License

Choose a license for your project and add the corresponding license file to the repository.

---

<p align="center">
  <b>Built with Python 🐍 | A Beginner Cybersecurity & Programming Micro Project</b>
</p>

<p align="center">
  ⭐ If you find this project useful, consider giving the repository a star!
</p>
