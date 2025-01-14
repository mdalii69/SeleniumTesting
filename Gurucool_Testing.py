from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Edge driver
driver = webdriver.Edge()
url = "https://www.gurucool.life/horoscope"
driver.get(url)
driver.maximize_window()

# Click on the login button
login = driver.find_element(By.XPATH, "//span[@class='select-none']")
login.click()

# Enter phone number and get OTP
number = "1234567890"
number_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter phone number']")
number_field.send_keys(number)
get_otp = driver.find_element(By.XPATH, "//button[normalize-space()='GET OTP']")
get_otp.click()

# Wait for user to enter OTP manually and click submit
time.sleep(30)  

# Click on the dropdown to for getting Virgo
dropdown_element = driver.find_element(By.CSS_SELECTOR, "body > main:nth-child(5) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")
dropdown_element.click()

# Click on the Virgo button
select_virgo = driver.find_element(By.CSS_SELECTOR, "body > main:nth-child(5) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(6)")
select_virgo.click()

# Check for the Virgo heading
virgo = driver.find_element(By.XPATH, "//h2[normalize-space()='Virgo']").text
try:
    assert virgo == "Virgo"
    print("Virgo Lucky Number accessed!")
except AssertionError:
    print("Virgo Lucky Number not accessed!")
    
# Wait before closing the driver
time.sleep(10)
driver.quit()
