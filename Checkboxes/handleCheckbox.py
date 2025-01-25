from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge()
browser.get('https://fs2.formsite.com/meherpavan/form2/index.html')
browser.maximize_window()
browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# For checking One Checkbox
browser.find_element(By.XPATH, '//label[normal-space()="Sunday"]').click()
time.sleep(3)

# For Unchecking that same Checkbox
browser.find_element(By.XPATH, '//label[normal-space()="Sunday"]').click()
time.sleep(3)

# For Checking All Checkboxes
checkboxes = browser.find_elements(By.XPATH, '//input[@type="checkbox"]')
for checkbox in checkboxes:
  checkbox.send_keys(Keys.SPACE)

# For Count of the Checkboxes
checked_count = 0
for checkbox in checkboxes:
  if checked.is_selected():
    checked_count+=1
expected_checked_count = 7

# Exception Handling
try:
  assert checked_count == expected_checked_count
  print('Checked Count Verified!')
except AssertionError:
  print('Checkbox Count Mismatched!')

# Closing Browser
finally:
  browser.quit()
