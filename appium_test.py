from appium import webdriver
from time import sleep

# Desired capabilities for the Flutter app
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'mytempavd',  # Replace with your target device name
    # 'app': '/home/vsts/work/1/s/build/app/outputs/flutter-apk/app-release.apk',
    'automationName': 'UiAutomator2',  # Add the missing comma here
    'appPackage': 'com.example.loginapp',  # Replace with your app's package name
    'appActivity': '.MainActivity',  # Replace with your app's main activity
    'autoGrantPermissions': True,
    'autoAcceptAlerts': True,
}

# Appium server URL
server_url = 'http://localhost:4723/wd/hub'

# Initialize the Appium driver with desired capabilities
driver = webdriver.RemoteCommand(command_executor=server_url, desired_capabilities=desired_caps)


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
if "Welcome" in welcome_text and "arun@gogosoon.com" in welcome_text:
    print("Login Successful!")
else:
    print("Login Failed!")

# Close the app
driver.quit()
