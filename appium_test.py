import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired capabilities for your Flutter app
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'mytempavd',
    'app': '/home/vsts/work/1/s/build/app/outputs/flutter-apk/app-release.apk'
}

# Initialize the Appium driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Define a function to perform login
def perform_login(email, password):
    # Wait for the email input field to be visible
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'email_input_id'))
    )
    email_input.send_keys(email)

    # Wait for the password input field to be visible
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'password_input_id'))
    )
    password_input.send_keys(password)

    # Wait for the Submit button to be clickable
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ACCESSIBILITY_ID, 'submit_button_id'))
    )
    submit_button.click()

# Test login functionality
try:
    # Replace 'your_email' and 'your_password' with actual login credentials
    perform_login('arun@gogosoon.com', 'qazxswedcvfr')

    # Wait for a few seconds to see the result
    time.sleep(5)

finally:
    # Close the app and end the Appium session
    driver.quit()
