from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeliveryLocation:
    def __init__(self, driver):
        self.driver = driver
        self.delivery_location_locator = (By.ID,"country")
        self.suggestion_locator = (By.XPATH,'//div[@class = "suggestions"]/ul/li/a[text()= "India"]')
        self.checkbox_tc_locator = (By.XPATH, "//label[@for='checkbox2']")
        self.purchase_locator = (By.XPATH, "//input[@type='submit']")
        self.success_msg_locator = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
        
        
    def click_delivery_location(self, text = "ind"):
        self.driver.find_element(*self.delivery_location_locator).send_keys(text)
    
    def click_suggestion(self):
         wait = WebDriverWait(self.driver , 10)
         wait.until(EC.element_to_be_clickable(self.suggestion_locator)).click()
         
    def click_checkbox_tc (self):
        self.driver.find_element(*self.checkbox_tc_locator).click()
        
    def click_purchase(self):
        self.driver.find_element(*self.purchase_locator).click()
        
    def verify_success_msg(self):
        wait = WebDriverWait(self.driver , 10)
        message = wait.until(EC.presence_of_element_located(self.success_msg_locator)).text
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in message
    
    
        
        
       
        