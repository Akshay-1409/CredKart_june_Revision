import allure
import pytest
from allure_pytest.utils import allure_title

from faker import Faker

from pageObjects.Registration_Page import Registration_Page_Class
from utilities.Logger import LoggerClass
from utilities.ReadConfig import Readconfig


@pytest.mark.usefixtures("setup")
class Test_Registration_002:
    log = LoggerClass.get_logger()
    register_url = Readconfig.get_registration_url()
    driver = None

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns=1, reruns_delays=1)
    #@allure_title("test_registration_002")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that user is able to refister to the application")
    def test_registration_002(self):
        self.log.info("test_registration_002 is started")
        self.log.info(f"Openint the registration page -->>{self.register_url}")
        self.driver.get(self.register_url)
        self.rp = Registration_Page_Class(self.driver)
        random_name = Faker().first_name()
        random_email = Faker().email()
        self.log.info(f"Enter name -->{random_name}")
        self.rp.Enter_name(random_name)
        self.log.info(f"Enter emai -->{random_email}")
        self.rp.Enter_email(random_email)
        self.log.info("Enter password")
        self.rp.Enter_password("Credencetest@123")
        self.log.info("Enter confirm password")
        self.rp.Enter_confirm_password("Credencetest@123")
        self.log.info("Clck register button")
        self.rp.Click_register()
        self.log.info("Verify registration")
        if self.rp.verify_menu() == "pass":
            self.log.info("test_registration_002 is passed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_registration_002_pass.png")
            self.log.info("Click Menu button")
            self.rp.Click_menu()
            self.log.info("Click logout button")
            self.rp.Click_logout()
            assert True
        else:
            self.log.info("test_registration_002 os failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_registration_002_fail.png")
            assert False
        self.log.info("test_registration_002 is completed")




