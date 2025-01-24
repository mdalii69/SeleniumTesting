from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Initialize the browser
browser = webdriver.Edge()
browser.get("https://the-internet.herokuapp.com/broken_images")
browser.maximize_window()

# Find all images on the page
images = browser.find_elements(By.TAG_NAME, "img")
broken_images = []

# Check each image's status
for image in images:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)

# Display results
if broken_images:
    print("List of broken images:", broken_images)
else:
    print("No broken images found.")

# Close the browser
browser.quit()
