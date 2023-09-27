import time
from appium import webdriver
from time import sleep

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
    # Locate and interact with the email input field using its ID
    email_input = driver.find_element_by_id('email_input_id')
    email_input.send_keys(email)

    # Locate and interact with the password input field using its ID
    password_input = driver.find_element_by_id('password_input_id')
    password_input.send_keys(password)

    # Locate and click the Submit button using its ID
    submit_button = driver.find_element_by_id('submit_button_id')
    submit_button.click()

# Test login functionality
try:
    # Replace 'your_email' and 'your_password' with actual login credentials
    perform_login('arun@gogosoon.com', 'qazxswedcvfr')

    # Wait for a few seconds to see the result
    sleep(5)

finally:
    # Close the app and end the Appium session
    driver.quit()
