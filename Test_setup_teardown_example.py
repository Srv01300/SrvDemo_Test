from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get("https://www.google.com")

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title == "Google"
    print("got tile info.")

def test_google_url():
    assert driver.current_url == "https://www.google.com/"
    print("Got url link")