import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# File Path for the CSV File
csv_file_path = "C:\\Users\\abc\\VS Code\\Testing\\test_data.csv"  # Ensure the file is in the same folder as your script.

# Load data from CSV
test_data = []
with open(csv_file_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        test_data.append(row)  # Append each row (username, password) to the list

print("Test Data Loaded:", test_data)  # Debug: Print the loaded test data

# Selenium WebDriver setup
driver = webdriver.Chrome()

# Iterate through test data and perform login
for data in test_data:
    username = data[0]
    password = data[1]

    # Open the target application
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(2)

    # Perform login
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Verify login and log out (if applicable)
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
