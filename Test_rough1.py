from selenium import webdriver
import pytest

@pytest.mark.usefixtures("init_driver")

class Test_demo:
    pass

class Test_google1(Test_demo):

  def test_google_title(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"
        print("google title")

class Test_google_url(Test_demo):
    def test_google_url(self):
        self.driver.get("https://www.youtube.com")
        assert self.driver.current_url.startswith("https://www.youtube.com")
        print("google url")
