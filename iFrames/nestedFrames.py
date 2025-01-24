from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
browser = webdriver.Edge()
browser.maximize_window()

# Open the URL with nested frames
browser.get("https://the-internet.herokuapp.com/nested_frames")

# Step 1: Switch to the top frame
browser.switch_to.frame("frame-top")  # Name or ID of the top frame

# Step 2: Switch to the middle frame inside the top frame
browser.switch_to.frame("frame-middle")  # Name or ID of the middle frame

# Step 3: Interact with the element inside the middle frame
middle_content = browser.find_element(By.ID, "content").text
print(f"Content in the middle frame: {middle_content}")

# Step 4: Return to the main content (outside all frames)
browser.switch_to.default_content()

# Step 5: Switch to the bottom frame
browser.switch_to.frame("frame-bottom")  # Name or ID of the bottom frame

# Step 6: Interact with the element inside the bottom frame
bottom_content = browser.find_element(By.TAG_NAME, "body").text
print(f"Content in the bottom frame: {bottom_content}")

# Quit the browser
browser.quit()
