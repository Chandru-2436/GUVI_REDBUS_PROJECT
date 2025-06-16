
# 🚌 Redbus Data Scraper & Filtering Dashboard

## 🔍 Project Overview
This project automates the extraction of real-time bus route data from [Redbus.in](https://www.redbus.in/) using **Selenium WebDriver** and visualizes it using an interactive dashboard built with **Streamlit**. It simulates a real-world travel aggregator use case — capturing live bus details like price, timing, seat availability, and ratings.

---

## ⚙️ Tech Stack

- **Python**
- **Selenium WebDriver**
- **SQLite** (for storing scraped data)
- **Streamlit** (for filtering & visualization)
- **ChromeDriver** (GUI-based, GUVI compliant)

---

## 📁 Project Structure

```
RedbusProject/
├── guvi_redbus_scraper_final.py      # Selenium scraper with manual input assist
├── streamlit_app.py                  # Interactive dashboard for filtering buses
├── bus_routes.db                     # SQLite database storing scraped routes
```

---

## 📌 Features

- Manual input of route using Redbus UI to comply with JavaScript restrictions
- Scrapes up to 3 buses per route: name, price, seats, rating, timings
- Saves structured data into `bus_routes.db`
- Streamlit dashboard:
  - Route-based filtering
  - Price slider
  - Minimum rating & seat availability filter
  - Clean tabular view of data

---

## 🧪 How to Run

### 🔹 Scraper

```bash
python guvi_redbus_scraper_final.py
```

1. Wait for Redbus to load in Chrome.
2. Manually enter **From**, **To**, and **Search**.
3. Press `ENTER` in the terminal when the results page loads.

### 🔹 Dashboard

```bash
streamlit run streamlit_app.py
```

---

## 🧾 Notes

- Designed to match **GUVI’s CodeKata / Mini Project 1** requirements
- Handles headless-blocking by using manual assist mode
- Simulates real use case for data extraction in dynamic web environments

---
