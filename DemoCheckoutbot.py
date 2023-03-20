import account

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class CheckOutBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.nike.com/")
        self.accept_cookies()

    def accept_cookies(self):
        button = self.driver.find_element_by_id("privacy-layer-accept-all-button")
        button.click()

    def login(self, email, password):

        #assuming that we put in valid creds from exisitn account, could also go guest checkout but this is to make it seamless
        self.driver.get("https://www.nike.com/login")
        time.sleep(5)
        email_input = self.driver.find_element_by_id("username")
        email_input.clear()
        email_input.send_keys(email)
        continue_button = self.driver.find_element_by_id("nds-btn css-ew3ocj btn-primary-dark  btn-md")
        continue_button.click()
        pass_input = self.driver.find_element_by_id("mms-login-form__password")
        pass_input.clear()
        pass_input.send_keys(password)
        self.driver.find_element_by_id("nds-btn css-ew3ocj btn-primary-dark  btn-md").click()

    def add_product_to_cart(self, link):
        self.driver.get(link)
        time.sleep(1)
        button = self.driver.find_element_by_css_selector(
            '[ncss-btn-primary-dark btn-lg add-to-cart-btn"]'
        )
        time.sleep(2)
        button.click()

    def checkout(self):
        self.driver.get("https://www.nike.com/cart")
        time.sleep(1)
        #go to checkout exisiting cart
        self.driver.find_elements_by_class_name(
            "css-10f2cr2-PrimaryDarkButton-buttonPaddingBorderRadiusStyles-disabledButtonStyles-primaryDisabledStyles-primaryDarkButtonStyles e1ets6350"
        )[2].click()
        time.sleep(1)
        #Select Member checkout
        self.driver.find_elements_by_class_name(
            "css-5w1jxa-PrimaryDarkButton-buttonPaddingBorderRadiusStyles-disabledButtonStyles-primaryDisabledStyles-primaryDarkButtonStyles e1udugn30"
        )[1].click()

        #assuming all account details have been filled, we go with exisisting ship method/address/Payment info
        #if guest, we would select elements to fill in forms but since this is example, were assuming valid creds/account are used
        # this is how you click the final checkout buttons, first review order, then place order
        self.driver.find_elements_by_class_name("nds-btn css-60b779 ex41m6f0 btn-primary-dark  btn-md")[2].click()
        self.driver.find_elements_by_class_name("nds-btn css-60b779 ex41m6f0 btn-primary-dark  btn-md").click()
    
    def __del__(self):
        self.driver.close()


if __name__ == "__main__":
    checkout_bot = CheckOutBot()

    checkout_bot.login(account.email, account.password)
    checkout_bot.add_product_to_cart(
        "https://www.nike.com/t/air-sport-2-golf-bag-B6jfrd/N1003477-698"
    )
    checkout_bot.checkout()