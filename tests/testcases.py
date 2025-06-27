from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select
import pytest
from pages.test_login import Test_Login
from BaseClass.baseclass import BaseClass
from pages.add_to_cart import Addtocart
from pages.finalcheckout import Final_Checkout
from pages.deliverylocation import DeliveryLocation

# @pytest.mark.usefixtures("setup")
class Test_01_Login(BaseClass):

    @pytest.mark.parametrize("username, password",[("rahulshettyacademy", "learning")])
    def test_login1(self, username, password):
        lp = Test_Login(self.driver)

        lp.enter_username(username)
        lp.enter_password(password)
        lp.click_checkbox()
        lp.click_signin()
        
        ac = Addtocart(self.driver)
        ac.click_addtocart()
        ac.click_checkout_btn()
        
        fc= Final_Checkout(self.driver)
        fc.click_final_checkout()
        
        dl = DeliveryLocation(self.driver)
        dl.click_delivery_location("ind")
        dl.click_suggestion()
        dl.click_checkbox_tc()
        dl.click_purchase()
        dl.verify_success_msg()
        
            # delivery_location = self.driver.find_element(By.ID, "country").send_keys("ind")
            # time.sleep(1)

            # wait = WebDriverWait(self.driver , 10)
            # wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, '//div[@class = "suggestions"]/ul/li/a[text()= "India"]'))).click()
            # time.sleep(1)

            # final_checkbox = self.driver.find_element(By. XPATH, "//label[@for='checkbox2']").click()
            # purchase = self.driver.find_element(By.XPATH," //input[@type='submit']").click()
            # time.sleep(1)
            # success_message = self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
            # print(success_message)


            # # Homebtn = driver.find_element(By.XPATH, "//a[normalize-space()='ProtoCommerce Home']").click()

            # # name = driver.find_element(By.XPATH,"//div[@class='form-group']//input[@name='name']").send_keys("Abbas")
            # # email = driver.find_element(By.XPATH,"//input[@name='email']").send_keys("Abbas@yahoo.com")
            # # password = driver.find_element(By.XPATH,"//input[@id='exampleInputPassword1']").send_keys("Abbas@7417")
            # # formCheckbox = driver.find_element(By.XPATH,"//input[@id='exampleCheck1']").click()
            # # gender = Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))

            # # gender.select_by_visible_text("Female")

            # # employement_status = driver.find_element(By.XPATH,"//input[@id='inlineRadio2']").click()
            # # print(employement_status)

            # # DOB =  driver.find_element(By.XPATH,"//input[@name='bday']").click()
            # # time.sleep(4)
        