import pytest
from selenium import webdriver


def test_yandex_login():
    driver = webdriver.Firefox()
    driver.get("https://passport.yandex.ru/auth/")
    username_input = driver.find_element_by_xpath("//input[@name='login']")
    password_input = driver.find_element_by_xpath("//input[@name='passwd']")
    submit_button = driver.find_element_by_xpath("//button[@type='submit']")

    username_input.send_keys("your_username")
    password_input.send_keys("your_password")
    submit_button.click()

    assert "Яндекс.Паспорт" in driver.title

    driver.quit()