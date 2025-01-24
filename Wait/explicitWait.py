from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Maximize Browser Window
driver.maximize_window()

# Navigate to the Website
driver.get("https://www.saucedemo.com/")

# Log In
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Use Explicit Wait for Hamburger Menu
wait = WebDriverWait(driver, 10)  # Timeout set to 10 seconds
hamburger_menu = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
hamburger_menu.click()

# Use Explicit Wait for Logout Link
logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
logout_link.click()

# Quit the browser
driver.quit()
