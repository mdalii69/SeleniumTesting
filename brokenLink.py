import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Target URL
url = "https://exactspace.co/"
driver.get(url)

# Fetch and print status code of the main website
try:
    main_response = requests.get(url)
    print(f"Main website: {url}, Status code: {main_response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error accessing {url}: {e}")

# Find all anchor tags
all_links = driver.find_elements(By.TAG_NAME, "a")
print(f"Total number of links on the page: {len(all_links)}")

# Loop through all links and validate
for link in all_links:
    href = link.get_attribute("href")  # Extract href attribute
    if href:
        try:
            response = requests.get(href)  # Send GET request
            if response.status_code >= 400:
                print(f"Broken link: {href}, Status code: {response.status_code}")
            else:
                print(f"Valid link: {href}, Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {href}: {e}")
    else:
        print("Link has no href attribute.")

# Close the browser
driver.quit()
