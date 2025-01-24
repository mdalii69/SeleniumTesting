from selenium import webdriver
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Define viewport resolutions
viewports = [
    (1024, 768),  # Desktop
    (768, 1024),  # Tablet Portrait
    (375, 667),   # Mobile Portrait
    (414, 896)    # Mobile Large Screen
]

try:
    for width, height in viewports:
        driver.set_window_size(width, height)
        time.sleep(2)  # Pause to observe each resolution
finally:
    driver.quit()  # Close browser
