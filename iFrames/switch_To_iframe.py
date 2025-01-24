from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
browser = webdriver.Edge()
browser.maximize_window()

# Open the target URL
browser.get("https://the-internet.herokuapp.com/iframe")

# Step 1: Switch to the IFrame
iframe = browser.find_element(By.ID, "mce_0_ifr")  # Locate the iframe by ID
browser.switch_to.frame(iframe)  # Switch to the iframe

# Step 2: Interact with an element inside the IFrame
editor = browser.find_element(By.ID, "tinymce")  # Locate the text editor
editor.clear()  # Clear existing text
editor.send_keys("This is a Selenium IFrame tutorial.")  # Enter new text

# Step 3: Return to the Main Content
browser.switch_to.default_content()  # Switch back to the main HTML

# Step 4: Interact with an element outside the IFrame
selenium_link = browser.find_element(By.LINK_TEXT, "Elemental Selenium")
selenium_link.click()  # Click the link

# Wait for a few seconds before closing
time.sleep(5)
browser.quit()
