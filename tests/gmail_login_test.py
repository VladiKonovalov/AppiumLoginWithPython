import time
from typing import Dict, Any

import pytest
from appium.options.common import AppiumOptions
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("userna:me, password, expected_result", [
    ("", "Password123", "failure"),
    ("student", "", "failure"),
    ("none", "none", "failure"),
    ("student", "Password123", "success")])
def test_login(username, password, expected_result):
    result = login(username, password)
    assert result == expected_result


def login(username, password):
    caps: Dict[str, Any] = {
        'platformName': 'Android',
        'deviceName': 'Android',
        "browserName": "Chrome",
        "automationName": "UiAutomator2"
    }
    # ios_caps = {
    #     'platformName': 'iOS',
    #     'deviceName': 'iOS',
    #     "browserName": "Safari",
    #     'automationName': 'XCUITest'
    # }

    # caps = android_caps if username.lower() == 'android' else ios_caps

    appiumUrl = 'http://localhost:4723/wd/hub'
    loginUrl = "https://practicetestautomation.com/practice-test-login/"
    driver = webdriver.Remote(appiumUrl, options=AppiumOptions().load_capabilities(caps))

    driver.get(loginUrl)

    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    time.sleep(3)
    # submit_button = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.ID, 'submit'))
    # )]
    print("Attempting to click on the submit button")

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()
    print("Clicked on the submit button successfully")
    time.sleep(7)

    result = "success" if driver.find_elements(By.LINK_TEXT, "Log out") else "failure"
    driver.quit()

    return result
