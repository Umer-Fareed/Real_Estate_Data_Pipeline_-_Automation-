# 🏠 Real Estate Data Pipeline & Automation

> Automated ETL pipeline for scraping real estate listings and storing structured data via Google Forms integration.

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green?logo=selenium)](https://selenium.dev)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.x-orange)](https://pypi.org/project/beautifulsoup4/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📌 Overview

This project implements a fully automated **ETL (Extract, Transform, Load) pipeline** for real estate data. It scrapes live property listings from **Zillow** — including addresses, prices, and listing URLs — and automatically submits the structured data into a **Google Form**, enabling seamless data collection and storage without manual input.

This is a practical demonstration of **web scraping**, **browser automation**, and **end-to-end data pipeline** engineering using Python.

---

## ✨ Features

- 🔍 **Web Scraping** — Extracts property addresses, prices, and listing links from Zillow in real time
- 🤖 **Browser Automation** — Uses Selenium WebDriver to handle dynamic JavaScript-rendered pages
- 📋 **Auto Form Submission** — Automatically fills and submits a Google Form for each scraped listing
- ⚙️ **Modular Design** — Clean, readable code with clearly separated scraping and submission logic
- 🔄 **End-to-End Pipeline** — Fully automated from data extraction to structured storage

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| **Language** | Python 3.9+ |
| **Browser Automation** | Selenium WebDriver |
| **HTML Parsing** | BeautifulSoup4 |
| **Data Source** | Zillow (web scraping) |
| **Data Storage** | Google Forms / Google Sheets |
| **Driver** | ChromeDriver |

---

## 🔄 Pipeline Architecture

```
┌─────────────────────┐
│   Zillow Website    │  ← Target data source
└─────────────────────┘
          │
          ▼
┌─────────────────────┐
│  Selenium WebDriver │  ← Loads JS-rendered page
└─────────────────────┘
          │
          ▼
┌─────────────────────┐
│   BeautifulSoup     │  ← Parses HTML, extracts:
│                     │    • Addresses
│                     │    • Prices
│                     │    • Listing URLs
└─────────────────────┘
          │
          ▼
┌─────────────────────┐
│  Data Structuring   │  ← Zips and aligns all fields
└─────────────────────┘
          │
          ▼
┌─────────────────────┐
│  Google Form Auto   │  ← Fills & submits each record
│  Submission         │    automatically
└─────────────────────┘
          │
          ▼
┌─────────────────────┐
│  Google Sheets      │  ← Structured, queryable data
└─────────────────────┘
```

---

## 📁 Project Structure

```
Real_Estate_Data_Pipeline_-_Automation-/
│
├── main.py          # Full ETL pipeline (scrape + submit)
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Google Chrome browser
- [ChromeDriver](https://chromedriver.chromium.org/) matching your Chrome version

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Umer-Fareed/Real_Estate_Data_Pipeline_-_Automation-.git
cd Real_Estate_Data_Pipeline_-_Automation-

# 2. Install dependencies
pip install selenium beautifulsoup4
```

### Configuration

Before running, update these two things in `main.py`:

**1. Set your ChromeDriver path:**
```python
chrome_driver_path = r"YOUR\PATH\TO\chromedriver.exe"
```

**2. Set your Google Form URL:**
```python
driver.get("YOUR_GOOGLE_FORM_URL_HERE")
```
> Make sure your Google Form has three text fields labeled: `Address`, `Price`, and `Link`

### Run

```bash
python main.py
```

The script will:
1. Open Zillow in a Chrome browser
2. Scrape all visible property listings
3. Auto-submit each listing to your Google Form
4. Print confirmation for each submitted record

---

## 📊 Sample Output

```
Loading Zillow...
Found 20 addresses, 20 prices, 20 links
Submitted: 123 Main St, San Francisco, CA | $1,200,000 | https://zillow.com/...
Submitted: 456 Oak Ave, San Francisco, CA | $985,000   | https://zillow.com/...
...
✅ All data submitted successfully!
```

---

## 🔧 Potential Extensions

- 📦 Store data directly in **CSV / PostgreSQL** instead of Google Forms
- ☁️ Deploy on **AWS Lambda** for scheduled scraping
- 📊 Connect to **Power BI / Looker Studio** for real-time dashboards
- 📬 Add **email/SMS alerts** via SMTP or Twilio when new listings appear
- 🔁 Add **pagination support** to scrape multiple pages

---

## ⚠️ Disclaimer

This project is built for **educational purposes** to demonstrate ETL pipeline and web automation skills. Always review and comply with a website's Terms of Service before scraping.

---

## 👨‍💻 Author

**H. M. Umar Fareed**
Data Scientist & ML Engineer | Published AI Researcher

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/h-m-umar-fareed)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/Umer-Fareed)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-green)](https://linktr.ee/Umer_fareed)
[![Email](https://img.shields.io/badge/Email-Contact-red)](mailto:fareedkamboh7@gmail.com)

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

> ⭐ If you find this project useful, please consider giving it a star!
