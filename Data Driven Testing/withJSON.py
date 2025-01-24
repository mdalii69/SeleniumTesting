import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

test_data = 'C:\\Users\\abc\\VS Code\\Testing\\test_data.json'
# Load JSON file
with open(test_data, "r") as file:
    data = json.load(file)

# Extract users from JSON
test_users = data["users"]  # Assuming JSON structure {"users": [{"username": ..., "password": ...}]}

# Initialize WebDriver
driver = webdriver.Chrome()

# Iterate through test users and perform login
for user in test_users:
    username = user["username"]
    password = user["password"]

    # Open the application
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(2)

    # Perform login
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Verify login and log out (optional)
    try:
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        print(f"Login successful for: {username}")
    except Exception as e:
        print(f"Login failed for: {username}. Error: {e}")
        continue

    time.sleep(2)

# Close the browser
driver.quit()
