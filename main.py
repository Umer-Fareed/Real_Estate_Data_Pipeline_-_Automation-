from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ---------------------- SETUP ----------------------
chrome_driver_path = r"C:\development\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

# ---------------------- SCRAPE ZILLOW ----------------------
print("Loading Zillow...")
driver.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/")
time.sleep(5)  # let page load fully

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Extract all links
all_link_elements = soup.select("a.list-card-link")
all_links = []
for link in all_link_elements:
    href = link.get("href")
    if href:
        if "http" not in href:
            all_links.append(f"https://www.zillow.com{href}")
        else:
            all_links.append(href)

# Extract all addresses
all_address_elements = soup.select("address")
all_addresses = [address.get_text() for address in all_address_elements]

# Extract all prices
all_price_elements = soup.select(".list-card-price")
all_prices = [price.get_text() for price in all_price_elements]

print(f"Found {len(all_addresses)} addresses, {len(all_prices)} prices, {len(all_links)} links")

# ---------------------- FILL GOOGLE FORM ----------------------
for address_text, price_text, link_text in zip(all_addresses, all_prices, all_links):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSciPLywlom78Z2vDr08JITvZuD8wChsxDxM3C0EWf9Ys-x1Qg/viewform")

    time.sleep(2)

    # Fill the form using aria-labels (make sure your form fields are named Address, Price, Link)
    address = driver.find_element(By.XPATH, '//input[@type="text" and @aria-label="Address"]')
    price = driver.find_element(By.XPATH, '//input[@type="text" and @aria-label="Price"]')
    link = driver.find_element(By.XPATH, '//input[@type="text" and @aria-label="Link"]')
    submit_button = driver.find_element(By.XPATH, '//span[text()="Submit"]/ancestor::div[@role="button"]')

    address.send_keys(address_text)
    price.send_keys(price_text)
    link.send_keys(link_text)

    submit_button.click()
    print(f"Submitted: {address_text} | {price_text} | {link_text}")
    time.sleep(1)

print("✅ All data submitted successfully!")
