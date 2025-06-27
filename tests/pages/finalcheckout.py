from selenium import webdriver
import time 
from selenium.webdriver.common.by import By

class Final_Checkout:
    def __init__(self,driver):
        self.driver = driver
        self.final_checkout_locator = (By.XPATH,"//button[@class = 'btn btn-success']")
        
    def click_final_checkout(self):
        self.driver.find_element(*self.final_checkout_locator).click()
        print("checkout")
        
         