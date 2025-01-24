from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import time

# Initialize WebDriver
browser = webdriver.Edge() 
browser.maximize_window()

# Open the website
url = "https://www.globalsqa.com/demo-site/datepicker/"
browser.get(url)

# Close any initial pop-up
browser.find_element(By.CLASS_NAME, "close_img").click()

# Switch to the frame containing the date picker
frameLo = browser.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")
browser.switch_to.frame(frameLo)
time.sleep(5)

# Locate the date picker input field
date_picker = browser.find_element(By.ID, "datepicker")
date_picker.click()

# Generate the desired date
# Current Date: datetime.now()
# Past Date (2 days ago): datetime.now() - timedelta(days=2)
# Future Date (7 days ahead): datetime.now() + timedelta(days=7)

current_date = datetime.now()
desired_date = current_date + timedelta(days=7)  # Change the delta as needed
formatted_date = desired_date.strftime("%m/%d/%Y")  # Format: MM/DD/YYYY

# Input the date into the text field
date_picker.clear()
date_picker.send_keys(formatted_date)
date_picker.send_keys(Keys.TAB)  # Tab out to confirm the input

# Verify the entered date
entered_date = date_picker.get_attribute("value")
print(f"Date entered: {entered_date}")

# Close the browser
time.sleep(3)
browser.quit()
