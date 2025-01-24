from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize WebDriver
browser = webdriver.Edge()
browser.maximize_window()

# Open the resizable element URL
url = "https://jqueryui.com/resizable/"
browser.get(url)

# Switch to the frame containing the resizable element
browser.switch_to.frame(browser.find_element(By.CSS_SELECTOR, "iframe.demo-frame"))

# Locate the resizable element and its corner
resizable_box = browser.find_element(By.ID, "resizable")
resizable_handle = browser.find_element(By.CSS_SELECTOR, ".ui-resizable-se")

# Get the initial size of the resizable element
initial_size = resizable_box.size
print(f"Initial Size: {initial_size}")

# Create ActionChains instance
actions = ActionChains(browser)

# Perform resizing action (drag the corner by offset)
actions.click_and_hold(resizable_handle).move_by_offset(90, 0).release().perform()
actions.click_and_hold(resizable_handle).move_by_offset(-90, 90).release().perform()

# Wait to observe the action
time.sleep(3)

# Get the resized dimensions of the element
resized_size = resizable_box.size
print(f"Resized Size: {resized_size}")

# Close the browser
browser.quit()
