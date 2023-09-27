from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

# Desired capabilities for the Flutter app
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'mytempavd',  # Replace with your target device name
    'app': 'build/app/outputs/flutter-apk/app-release.apk',  # Replace with the path to your app APK file
    'automationName': 'UiAutomator2'
}

# Appium server URL
server_url = "http://127.0.0.1:4723/wd/hub"

# Initialize the Appium driver
driver = webdriver.Remote(server_url, desired_caps)

# Wait for the app to launch
sleep(5)

# Find the email and password text fields
email_field = driver.find_element_by_id("emailController")
password_field = driver.find_element_by_id("passwordController")

# Enter the login credentials
email_field.send_keys("arun@gogosoon.com")
password_field.send_keys("qazxswedcvfr")

# Perform the login action
submit_button = driver.find_element_by_id("submitButton")
submit_button.click()

# Wait for the login process to complete
sleep(5)

# Verify if the login was successful
welcome_text = driver.find_element_by_id("emailText").text
if welcome_text == "Welcome, arun@gogosoon.com!":
    print("Login Successful!")
else:
    print("Login Failed!")

# Close the app
driver.quit()
