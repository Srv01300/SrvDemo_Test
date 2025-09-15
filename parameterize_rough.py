from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.usefixtures("init_driver")
class Base_test:
    pass

class Test_Hubspot(Base_test):

    @pytest.mark.parametrize("Emailaddress, Password",
                                            [
                                                ("abc@gmail.com", "12345"), ("Siri@gmail.com", "siri123")
                                            ]
                                            )

    def test_login_hubspot(self, Emailaddress,  Password):

        self.driver.get("https://app.hubspot.com/login/legacy")
        self.driver.find_element(By.ID, 'username').send_keys(Emailaddress)
        time.sleep(3)
        self.driver.find_element(By.ID, 'password').send_keys(Password)
        time.sleep(3)
        print("login test completed")
