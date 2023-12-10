import time
from telnetlib import EC
from typing import Dict, Any

import pytest
from appium.options.common import AppiumOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    appiumUrl = 'http://localhost:4723/wd/hub'
    loginUrl = "https://practicetestautomation.com/practice-test-login/"
    caps: Dict[str, Any] = {
        'platformName': 'Android',
        'deviceName': 'Android',
        "browserName": "Chrome",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote(appiumUrl, options=AppiumOptions().load_capabilities(caps))
    driver.get(loginUrl)
    yield driver
    driver.quit()


@pytest.mark.parametrize("username, password, expected_result", [
    ("", "Password123", "failure"),
    ("student", "", "failure"),
    ("none", "none", "failure"),
    ("student", "Password123", "success")
])
def test_login(driver, username, password, expected_result):
    # caps = android_caps if username.lower() == 'android' else ios_caps

    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    time.sleep(3)

    print("Attempting to click on the submit button")
    # submit_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.ID, 'submit'))
    # )

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    print("Clicked on the submit button successfully")
    time.sleep(7)

    result = "success" if driver.find_elements(By.LINK_TEXT, "Log out") else "failure"

    assert result == expected_result
