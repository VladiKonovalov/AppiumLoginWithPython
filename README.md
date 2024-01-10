Appium Login Test Automation

Overview
This project demonstrates automated testing of a login functionality using Appium and Selenium. The tests are designed to run on an Android device using the Chrome browser.

Setup
Prerequisites:

Ensure you have Python installed.
Install required dependencies using pip install -r requirements.txt.
Appium Server:

Start the Appium server with the command appium.
Test Execution:

Run the tests using the command pytest test_login.py.

Configuration

Appium URL: http://localhost:4723/wd/hub

Login URL: https://practicetestautomation.com/practice-test-login/

Test Scenarios
The project includes the following test scenarios:

Empty Username: Validates login failure with an empty username.
Empty Password: Validates login failure with an empty password.
Invalid Credentials: Validates login failure with invalid credentials.
Successful Login: Validates successful login with valid credentials.
Test Execution
The tests use the Appium server to interact with the login page, input credentials, and verify the login result.

Test Structure
test_login.py: Contains the test cases.
conftest.py: Defines fixtures used in the tests.
Usage
Feel free to customize the tests for your specific application by modifying the test parameters and logic in test_login.py.

