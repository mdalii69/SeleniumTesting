from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
browser = webdriver.Edge()
browser.maximize_window()

# Open First Tab (Selenium website)
browser.get("https://www.selenium.dev")

# Open Second Tab (Playwright website)
browser.switch_to.new_window('tab')
browser.get("https://playwright.dev")

# Count Open Tabs
tabs = browser.window_handles
print("Number of tabs:", len(tabs))

# Switch to First Tab and Perform Action
first_tab = tabs[0]
browser.switch_to.window(first_tab)
download_link = browser.find_element(By.XPATH, "//a[@href='/downloads']")
download_link.click()
time.sleep(2)

# Switch to Second Tab and Perform Action
second_tab = tabs[1]
browser.switch_to.window(second_tab)
get_started_link = browser.find_element(By.CSS_SELECTOR, ".getStarted_Sjon")
get_started_link.click()
time.sleep(2)

# Close browser
browser.quit()
