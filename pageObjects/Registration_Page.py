
from pageObjects.Login_Page import LoginPage_Class
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Registration_Page_Class(LoginPage_Class):
    text_name_id = "name"
    text_confirm_password_id = "password-confirm"
    button_class = "btn"


    def Enter_name(self,name):
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, self.text_name_id)))
        self.driver.find_element(By.ID, self.text_name_id).clear()
        self.driver.find_element(By.ID, self.text_name_id).send_keys(name)


    def Enter_confirm_password(self, password):
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, self.text_confirm_password_id)))
        self.driver.find_element(By.ID, self.text_confirm_password_id).clear()
        self.driver.find_element(By.ID, self.text_confirm_password_id).send_keys(password)


    def Click_register(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, self.button_class)))
        self.driver.find_element(By.CLASS_NAME, self.button_class).click()


