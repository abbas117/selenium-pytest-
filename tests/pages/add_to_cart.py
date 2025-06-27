from selenium.webdriver.common.by import By
import time
class Addtocart:
    def __init__(self, driver):
        self.driver = driver
        self.addtocart_locator = (By.XPATH, "//div[@class='card h-100']")
        self.title_locator = (By.XPATH,".//h4")
        self.cart_locator = (By.XPATH, ".//button")
        self.checkout_btn_locator = (By.XPATH, "//a[@class= 'nav-link btn btn-primary']")
        
    def click_addtocart(self):
        item_list = ["iphone X","Samsung Note 8"]
        addtocart_element = self.driver.find_elements(*self.addtocart_locator)
        print(len(addtocart_element))
        
        for card in addtocart_element:
            title = card.find_element(*self.title_locator).text.strip()
            if title in item_list:
                card.find_element(*self.cart_locator).click()
                print(f"Added to cart: {title}")
                time.sleep(2)
    def click_checkout_btn(self):
        self.driver.find_element(*self.checkout_btn_locator).click()
        print("checkout button clicked")
        
        