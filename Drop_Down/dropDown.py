from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Edge()
driver.maximize_window()
login_url = 'https://the-internet-herokuapp.com/dropdown'
driver.get(login_url)

dropdown_element = driver.find_element(By.ID, "dropdown")
select = Select(dropdown_element)

# Select the value by visible text
select.select_by_visible_text("Option 2")
time.sleep(2)

# Select the value by index
select.select_by_index(2)
time.sleep(2)

# Select the option by using a value
select.select_by_value("2")
time.sleep(2)

# Verifying Options Count
option_count = len(select.options)
expected_count = 3
assert expected_count == option_count

# Selecting option and Checking between Multiple
target_value = "Option 2"
for option in select.options:
  if option.text == target_value:
    option.click()
    print(f'Selected Option is {target_value}')
    break
  else:
    print(f'Option "{target_value}" not found')

driver.quit()
