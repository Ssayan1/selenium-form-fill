from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time
import re

# === Setup Chrome driver ===
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # keeps Chrome open after script ends
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

# Wait for page load
sleep(3)

# === Handle initial popups ===
print("Looking for language selection...")
try:
    language_button = driver.find_element(By.ID, "langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    sleep(3)  # wait for reload
except NoSuchElementException:
    print("Language selection not found")

sleep(2)  # extra wait

# === Find the big cookie ===
cookie = driver.find_element(By.ID, "bigCookie")

# Track store items (products 0–17)
item_ids = [f"product{i}" for i in range(18)]

# === Timers ===
wait_time = 5  # start checking store every 5s
timeout = time() + wait_time

print("Bot started...")

while True:
    # Click the cookie fast
    for _ in range(50):  # 50 clicks per loop iteration
        cookie.click()

    # Every `wait_time` seconds, check for purchases
    if time() > timeout:
        try:
            # --- Get current cookies ---
            cookies_element = driver.find_element(By.ID, "cookies")
            cookie_text = cookies_element.text.replace(",", "")
            cookie_count = int(re.search(r"\d+", cookie_text).group())

            # --- Buy upgrades first (priority!) ---
            upgrades = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
            for upgrade in upgrades:
                try:
                    upgrade.click()
                    print("Bought an upgrade!")
                except:
                    pass

            # --- Buy most expensive product we can afford ---
            products = driver.find_elements(By.CSS_SELECTOR, "div.product.unlocked.enabled")
            if products:
                best_item = products[-1]  # last = most expensive
                item_id = best_item.get_attribute("id")
                best_item.click()
                print(f"Bought product: {item_id}")

            # --- Adjust wait time dynamically ---
            wait_time = max(5, cookie_count // 50)
            timeout = time() + wait_time

        except Exception as e:
            print(f"Error during purchase check: {e}")

    # (optional) you can break after X minutes if needed
    # if time() > time_limit:
    #     break
