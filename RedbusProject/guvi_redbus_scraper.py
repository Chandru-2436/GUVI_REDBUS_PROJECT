
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import sqlite3

# Set up database connection
conn = sqlite3.connect("bus_routes.db")
cursor = conn.cursor()

# Set up Selenium Chrome in GUI mode
options = Options()
options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Route info (for inserting to DB only)
source = "Chennai"
dest = "Bangalore"

try:
    print("🔓 Opening Redbus — please manually enter source, destination, and click 'Search'")
    driver.get("https://www.redbus.in/")

    # Pause for manual input
    input("📌 After you enter Source, Destination, pick date, and click Search, press ENTER here to continue...")

    # Wait for bus items
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "bus-items")))
    time.sleep(2)

    buses = driver.find_elements(By.CLASS_NAME, "bus-item")
    if not buses:
        print("⚠️ No buses found. Please make sure you completed the search manually.")
    else:
        for bus in buses[:3]:
            try:
                name = bus.find_element(By.CLASS_NAME, "travels").text
                btype = bus.find_element(By.CLASS_NAME, "bus-type").text
                dep = bus.find_element(By.CLASS_NAME, "dp-time").text
                arr = bus.find_element(By.CLASS_NAME, "bp-time").text
                dur = bus.find_element(By.CLASS_NAME, "dur").text
                price = bus.find_element(By.CLASS_NAME, "fare").text.strip("₹").strip()
                rating = bus.find_element(By.CLASS_NAME, "rating-sec").text.strip() or "0"
                seats = bus.find_element(By.CLASS_NAME, "seat-left").text.strip().split()[0]

                cursor.execute("""
                INSERT INTO bus_routes (route_name, route_link, busname, bustype, departing_time, duration, reaching_time, star_rating, price, seats_available)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    f"{source} to {dest}",
                    driver.current_url,
                    name, btype, dep, dur, arr, float(rating), float(price), int(seats)
                ))
                print(f"✅ {name} | ₹{price} | {dep} → {arr}")
            except Exception as e:
                print(f"⚠️ Error scraping a bus: {e}")
        conn.commit()
        print("✅ Buses scraped and saved to database.")

except Exception as e:
    print(f"❌ Error: {e}")

driver.quit()
conn.close()
print("✅ Script finished.")
