import time
from appium import webdriver

# Desired capabilities for your Flutter app
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'mytempavd',
    'app': '/home/vsts/work/1/s/build/app/outputs/flutter-apk/app-release.apk',
}

# Initialize the Appium driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Define a function to perform login
def perform_login(email, password):
    # Wait for the email input field to be visible and interact with it
    driver.find_element_by_accessibility_id('email_input_id').send_keys(email)

    # Wait for the password input field to be visible and interact with it
    driver.find_element_by_accessibility_id('password_input_id').send_keys(password)

    # Wait for the Submit button to be clickable and click it
    driver.find_element_by_accessibility_id('submit_button_id').click()

# Test login functionality
try:
    # Replace 'your_email' and 'your_password' with actual login credentials
    perform_login('arun@gogosoon.com', 'qazxswedcvfr')

    # Wait for a few seconds to see the result
    time.sleep(5)

finally:
    # Close the app and end the Appium session
    driver.quit()
