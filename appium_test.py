from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

# Desired capabilities for the Flutter app
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'mytempavd',  # Replace with your target device name
    'app': '/home/vsts/work/1/s/build/app/outputs/flutter-apk/app-release.apk',
    'automationName': 'UiAutomator2'
}

# Appium server URL
server_url = "http://127.0.0.1:4723/wd/hub"

# Initialize the Appium driver
driver = webdriver.Remote(server_url, desired_caps)

# Wait for the app to launch
sleep(5)

# Find the email and password text fields
email_field = driver.find_element_by_id("email_input_id")  # Assuming this is the correct ID
password_field = driver.find_element_by_id("password_input_id")  # Assuming this is the correct ID

# Enter the login credentials
email_field.send_keys("arun@gogosoon.com")
password_field.send_keys("qazxswedcvfr")

# Perform the login action
submit_button = driver.find_element_by_id("submit_button_id")  # Assuming this is the correct ID
submit_button.click()

# Wait for the login process to complete
sleep(5)

# Verify if the login was successful
welcome_text = driver.find_element_by_id("homepageText")  # Assuming this is the correct ID
if welcome_text.text == "Welcome, arun@gogosoon.com!":
    print("Login Successful!")
else:
    print("Login Failed!")

# Close the app
driver.quit()
