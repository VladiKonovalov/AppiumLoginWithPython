from typing import Dict, Any

import pytest
from appium.options.common import AppiumOptions
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("username, password, expected_result", [
    ("student", "Password123", "success")
])
def test_login(username, password, expected_result):
    result = login(username, password)
    assert result == expected_result


def login(username, password):
    cap: Dict[str, Any] ={
        'platformName': 'Android',
        'deviceName': 'Android',
        "browserName": "Chrome",
        "automationName": "UiAutomator2",
        "chromedriverExecutable": "/path/to/chromedriver"
    # 'appPackage': 'com.hmh.api',
        #  'appActivity': '.ApiDemos'
        # 'language': 'en',
        # 'locale': 'US'
    }

    appiumUrl = 'http://localhost:4723/wd/hub'
    loginUrl = "https://practicetestautomation.com/practice-test-login/"
    driver = webdriver.Remote(appiumUrl, options=AppiumOptions().load_capabilities(cap))

    driver.get(loginUrl)

    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    result = "success" if driver.find_elements(By.LINK_TEXT, "Log out") else "failure"
    driver.quit()

    return result
