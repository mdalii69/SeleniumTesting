from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
browser = webdriver.Edge()
browser.maximize_window()
browser.get("https://cosmocode.io/automation-practice-webtable/")  # Replace with the actual URL

# Scroll to make the table visible
browser.execute_script("window.scrollTo(0, 700);")

# Locate the table
table = browser.find_element(By.ID, "countries")  # Replace with the actual ID

# Find all rows in the table
rows = table.find_elements(By.TAG_NAME, "tr")
row_count = len(rows) - 1  # Exclude header row

print(f"Number of rows in the table (excluding header): {row_count}")

# Target value to search
target_value = "India"
found = False

# Loop through rows and cells to find the target value
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if target_value in cell.text:
            print(f"Value found: {cell.text}")
            found = True
            break
    if found:
        break

if not found:
    print(f"Target value '{target_value}' not found in the table.")

# Close the browser
browser.quit()
