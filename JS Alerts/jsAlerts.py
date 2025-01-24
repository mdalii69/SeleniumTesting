from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
browser = webdriver.Edge()
browser.maximize_window()

# Open the webpage containing JavaScript alerts
browser.get("https://the-internet.herokuapp.com/javascript_alerts")

# Handle the Simple Alert
print("\nHandling Simple Alert:")
alert_button = browser.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
alert_button.click()

# Switch to the alert and accept it
alert = browser.switch_to.alert
print(f"Alert Text: {alert.text}")
alert.accept()
print("Simple alert accepted.")

time.sleep(2)

# Handle the Confirmation Alert
print("\nHandling Confirmation Alert:")
confirm_button = browser.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_button.click()

# Switch to the alert, print its text, and dismiss it
alert = browser.switch_to.alert
print(f"Alert Text: {alert.text}")
alert.dismiss()  # Clicks "Cancel"
print("Confirmation alert dismissed.")

time.sleep(2)

# Handle the Prompt Alert
print("\nHandling Prompt Alert:")
prompt_button = browser.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
prompt_button.click()

# Switch to the alert, send text, and accept it
alert = browser.switch_to.alert
print(f"Alert Text: {alert.text}")
alert.send_keys("This is a test input.")
alert.accept()  # Clicks "OK"
print("Prompt alert accepted with input.")

time.sleep(2)

# Close the browser
browser.quit()
