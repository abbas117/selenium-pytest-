from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import pytest

@pytest.fixture(autouse=True, scope="class")
def setup(request):
    driver = webdriver.Edge()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    time.sleep(2)
    request.cls.driver = driver
    print(driver.title)
    driver.implicitly_wait(5)
    yield
    driver.quit()
   
