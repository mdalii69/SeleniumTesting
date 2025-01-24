from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize WebDriver
browser = webdriver.Edge()
browser.maximize_window()

# Open the URL
url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)

# Create ActionChains object
actions = ActionChains(browser)

# Locate the "Switch To" menu
hover_element = browser.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")

# Hover over the "Switch To" menu
actions.move_to_element(hover_element).perform()
time.sleep(2)  # Wait to see the hover effect

# Click on "Frames" after hovering
frames_option = browser.find_element(By.XPATH, "//a[normalize-space()='Frames']")
frames_option.click()

# Verification: Ensure navigation to the Frames page
try:
    assert "Frames" == browser.title
    print("Successfully navigated to Frames page!")
except AssertionError:
    print("Failed to navigate to Frames page!")

# Clean up: Close the browser
finally:
    time.sleep(3)
    browser.quit()
