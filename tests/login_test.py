import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By


@pytest.mark.parametrize("username, password, expected_result", [
    ("", "Password123", "failure"),
    ("student", "", "failure"),
    ("none", "none", "failure"),
    ("student", "Password123", "success")

])
def test_login(username, password, expected_result):
    result = login(username, password)
    assert result == expected_result


def login(username, password):
    driver = webdriver.Edge()

    driver.get("https://practicetestautomation.com/practice-test-login/")

    username_input = driver.find_element("id", 'username')
    username_input.send_keys(username)

    password_input = driver.find_element("id", 'password')
    password_input.send_keys(password)

    submit_button = driver.find_element("id", 'submit')
    submit_button.click()
    result = "success" if driver.find_elements(By.LINK_TEXT, "Log out") else "failure"
    driver.quit()

    return result
