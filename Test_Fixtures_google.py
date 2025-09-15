from selenium import webdriver
import time
import pytest

driver = None

@pytest.fixture(scope = 'module')
def init__driver():
    global driver
    print("-----setup----")
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get("https://www.google.com/")

    yield
    print("------teardown-----")
    driver.quit()

@pytest.mark.usefixtures("init__driver")
def test_google_title():
    assert driver.title == "Google"
    print("test1 title success")

@pytest.mark.usefixtures("init__driver")
def test_google_url():
    assert driver.current_url.startswith("https://www.google.com")
    print("url testcase success")

