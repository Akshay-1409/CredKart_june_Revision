import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select


from pageObjects.Login_Page import LoginPage_Class


class Checkout_Class(LoginPage_Class):

    click_product_xpath = "//h3[normalize-space()='Apple Macbook Pro']"
    click_add_to_cart_css = "input[value='Add to Cart']"
    click_proceed_to_checkout_xpath = "/html[1]/body[1]/div[1]/a[2]"
    text_first_name_xpath = "//input[@id='first_name']"
    text_last_name_xpath = "//input[@id='last_name']"
    text_phone_xpath = "//input[@id='phone']"
    text_address_xpath = "//textarea[@id='address']"
    text_zip_xpath = "//input[@id='zip']"
    dropdown_state ="//select[@id='state']"
    text_owner_name_xpath = "//input[@id='owner']"
    text_cvv_xpath = "//input[@id='cvv']"
    text_card_number_xpath = "//input[@id='cardNumber']"
    dropdown_year = "//select[@id='exp_year']"
    dropdown_month ="//select[@id='exp_month']"
    click_continue_checkout_xpath = "//button[@id='confirm-purchase']"
    message_xpath = "//p[@class='w-lg-50 mx-auto']"


    def Click_product(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,self.click_product_xpath)))
        self.driver.find_element(By.XPATH, self.click_product_xpath).click()


    def Click_add_to_cart(self):
        time.sleep(2)
        self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self.click_add_to_cart_css)))
        self.driver.find_element(By.CSS_SELECTOR, self.click_add_to_cart_css).click()


    def Click_proceed_to_checkout(self):
        #time.sleep(2)
        #self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.click_proceed_to_checkout_Xpath)))
        proceed_to_checkout = self.driver.find_element(By.XPATH, self.click_proceed_to_checkout_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", proceed_to_checkout)
        proceed_to_checkout.click()



    def Enter_first_name(self,name):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.text_first_name_xpath)))
        self.driver.find_element(By.XPATH, self.text_first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_first_name_xpath).send_keys(name)

    def Enter_last_name(self,name):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.text_last_name_xpath)))
        self.driver.find_element(By.XPATH, self.text_last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_last_name_xpath).send_keys(name)\

    def Enter_phone(self,phone):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.text_phone_xpath)))
        self.driver.find_element(By.XPATH, self.text_phone_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_phone_xpath).send_keys(phone)


    def Enter_address(self, address):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.text_address_xpath)))
        self.driver.find_element(By.XPATH, self.text_address_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_address_xpath).send_keys(address)

    def Enter_zip(self, zip):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.text_zip_xpath)))
        self.driver.find_element(By.XPATH, self.text_zip_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_zip_xpath).send_keys(zip)


    def Select_state(self, state):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.dropdown_state)))
        dropdown_state = Select(self.driver.find_element(By.XPATH, self.dropdown_state))
        dropdown_state.select_by_visible_text(state)


    def Enter_owner_name(self, name):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.text_owner_name_xpath)))
        self.driver.find_element(By.XPATH, self.text_owner_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_owner_name_xpath).send_keys(name)


    def Enter_cvv_number(self, cvv):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.text_cvv_xpath)))
        self.driver.find_element(By.XPATH, self.text_cvv_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_cvv_xpath).send_keys(cvv)


    def Enter_card_number(self, card_number):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.text_card_number_xpath)))
        self.driver.find_element(By.XPATH, self.text_card_number_xpath).send_keys(card_number)


    def Select_year(self, year):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.dropdown_year)))
        dropdown_year = Select(self.driver.find_element(By.XPATH, self.dropdown_year))
        dropdown_year.select_by_visible_text(year)



    def Select_month(self, month):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.dropdown_month)))
        dropdown_month = Select(self.driver.find_element(By.XPATH, self.   dropdown_month))
        dropdown_month.select_by_visible_text(month)



    def Click_continue_checkout(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.click_continue_checkout_xpath)))
        self.driver.find_element(By.XPATH, self.click_continue_checkout_xpath).click()


    def Get_message(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.message_xpath)))
        return self.driver.find_element(By.XPATH, self.message_xpath).text




















