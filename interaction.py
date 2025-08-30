from selenium import webdriver
from selenium.webdriver.common.by import By

# Create ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Launch browser
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Locate fields
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email_address = driver.find_element(By.NAME, "email")

# Fill form
first_name.send_keys("Sayan")
last_name.send_keys("Sanki")
email_address.send_keys("sayan@gmail.com")

# Submit
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
