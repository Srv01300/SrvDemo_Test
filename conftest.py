from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time

@pytest.fixture(params = ['Chrome', 'Firefox' ], scope = 'class')
def init_driver(request):
    if request.param == 'Chrome':
        webdriver1 = webdriver.Chrome()
    if request.param == 'Firefox':
        webdriver1 = webdriver.Firefox()
    request.cls.driver = webdriver1
    yield
    webdriver1.close()


