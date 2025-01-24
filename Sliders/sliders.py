from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize WebDriver
browser = webdriver.Edge()
browser.maximize_window()

# Open the slider URL
url = "https://the-internet.herokuapp.com/horizontal_slider"
browser.get(url)

# Locate the slider element
slider = browser.find_element(By.XPATH, "//input[@type='range']")

# Create an ActionChains object
actions = ActionChains(browser)

# Click and hold the slider (click_and_hold()), 
# move it by an offset (move_by_offset(x, y)), 
# then release it (release())
actions.click_and_hold(slider).move_by_offset(60, 0).release().perform()   # Move the slider to the right
actions.click_and_hold(slider).move_by_offset(-60, 0).release().perform()  # Move the slider to the left

# Wait to observe the action
time.sleep(3)

# Close the browser
browser.quit()
