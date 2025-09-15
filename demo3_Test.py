import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def testadd_m1():
    add1 = 100
    assert(add1)


def test_google():
    driver1= webdriver.Chrome()
    driver1.get("https://google.com")
    assert driver1.title == "Google"
    time.sleep(3)
    driver1.quit()

def test_gmail():
    driver2 = webdriver.Chrome()
    driver2.get("https://gmail.com")
    assert driver2.title == "Gmail"
    driver2.quit()


