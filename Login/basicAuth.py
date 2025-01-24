from selenium import webdriver
import time

# Credentials for authentication
username = "admin"
password = "admin"

# URL with embedded credentials
url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"

# Initialize WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to the URL
driver.get(url)

# Wait to observe the result
time.sleep(5)

# Validate successful login by checking the message
success_message = driver.find_element("tag name", "p").text
print(f"Success Message: {success_message}")

# Close the browser
driver.quit()
