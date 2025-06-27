from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select
import pytest

class Test_Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, "username")
        self.password_locator = (By.ID, "password")
        self.checkbox_locator = (By.XPATH, '//input[@type = "checkbox"]')
        self.signin_locator = (By.XPATH, "//input[@id='signInBtn']")
        
    def enter_username(self, username):
        element = self.driver.find_element(*self.username_locator)
        element.clear()
        element.send_keys(username)
        
    def enter_password(self, password):
        element = self.driver.find_element(*self.password_locator)
        element.clear()
        element.send_keys(password)
        
    def click_checkbox(self):
        self.driver.find_element(*self.checkbox_locator).click()
        
    def click_signin(self):
        self.driver.find_element(*self.signin_locator).click()
        
        
