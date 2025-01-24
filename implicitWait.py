from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Set Implicit Wait
driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to be present or interactable

# Maximize Window and Open URL
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Perform Login
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Access Hamburger Menu and Log Out
hamburger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
hamburger_menu.click()

logout_link = driver.find_element(By.ID, "logout_sidebar_link")
logout_link.click()

# Quit the driver
driver.quit()
