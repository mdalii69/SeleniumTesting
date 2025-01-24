from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize WebDriver
browser = webdriver.Edge()  # Or use Edge/Firefox
browser.maximize_window()

# Open the URL
url = "https://the-internet.herokuapp.com/drag_and_drop"
browser.get(url)

# Locate the source and destination elements
source_element = browser.find_element(By.ID, "column-a")
destination_element = browser.find_element(By.ID, "column-b")

# Create ActionChains object
actions = ActionChains(browser)

# Perform drag and drop
actions.drag_and_drop(source_element, destination_element).perform()

# Wait to observe the result
time.sleep(3)

# Close the browser
browser.quit()

