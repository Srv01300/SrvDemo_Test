from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_driver1_google():
    driver1 = webdriver.Chrome()
    driver1.get("https://google.com")
    time.sleep(2)
    assert driver1.title == "Google"
    time.sleep(4)
    driver1.quit()



def test_driver2_youtube():
    driver2 = webdriver.Chrome()
    driver2.get("https://youtube.com")
    assert driver2.get_cookies()
    time.sleep(3)
    driver2.quit()
def test_driver3_facebook():
    driver3 = webdriver.Chrome()
    driver3.get("https://facebook.com")
    assert driver3.title == "Facebook - log in or sign up"
    time.sleep(4)
    driver3.quit()
