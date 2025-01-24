from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta
import time

# Initialize WebDriver
browser = webdriver.Edge()
browser.maximize_window()

# Open the URL
url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)

# Locate and click the date picker input to open the calendar
date_picker = browser.find_element(By.ID, "datepicker2")
date_picker.click()
time.sleep(5)

# Calculate the desired date (example: future date +7 days)
current_date = datetime.now()
desired_date = current_date + timedelta(days=7)

# Extract day, month, and year for selection
day = desired_date.day
month = desired_date.strftime("%B")  # Full month name (e.g., "March")
year = desired_date.year

# Handle the month dropdown
month_dropdown = Select(browser.find_element(By.XPATH, "//select[@title='Change the month']"))
month_dropdown.select_by_visible_text(month)  # Select month by visible text

# Handle the year dropdown
year_dropdown = Select(browser.find_element(By.XPATH, "//select[@title='Change the year']"))
year_dropdown.select_by_visible_text(str(year))  # Select year by visible text

# Select the day from the calendar
day_element = browser.find_element(By.LINK_TEXT, str(day))
day_element.click()

# Verification: Ensure the selected date is set in the input field
selected_date = date_picker.get_attribute("value")
print(f"Selected Date: {selected_date}")

# Clean up: Close the browser
time.sleep(3)
browser.quit()