from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Create an Options object for Chrome
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Add incognito mode argument

# Initialize WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Maximize window and open a website
driver.maximize_window()
driver.get("https://www.google.com")

# Wait for observation
time.sleep(5)

# Close the browser
driver.quit()
