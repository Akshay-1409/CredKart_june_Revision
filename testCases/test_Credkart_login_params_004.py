import allure
import pytest


from pageObjects.Login_Page import LoginPage_Class
from utilities.Logger import LoggerClass
from utilities.ReadConfig import Readconfig


@pytest.mark.usefixtures("setup")
class Test_Login_params_002:
    log = LoggerClass.get_logger()
    login_url = Readconfig.get_login_url()
    driver = None
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns =1, resuns_delay=1)
    @allure.title("test_verify_login_param_005")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("verify that user is able to login to the application")

    def test_verify_login_param_005(self,data_for_login):
        self.log.info ("test_verify_login_param_005 is started")
        self.log.info(f"Opening the login page-->{self.login_url}")
        self.driver.get(self.login_url)
        self.lp = LoginPage_Class(self.driver)
        email = data_for_login[0]
        password = data_for_login[1]
        expected_result = data_for_login[2]
        self.log.info(f"Enter email -->{email}")
        self.lp.Enter_email(email)
        self.log.info(f"enter password -->{password}")
        self.lp.Enter_password(password)
        self.log.info("Clicking Login button")
        self.lp.Click_login()
        self.log.info("verify login")
        if self.lp.verify_menu() =="pass":
            self.log.info("login pass")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(f".\\Screenshots\\test_verify_login_param_005_login_pass_{email}_{password}.png")
            self.log.info("Click menu button")
            self.lp.Click_menu()
            self.log.info("Click logout button")
            self.lp.Click_logout()
            actual_result = "login pass"
        else:
            self.log.info("login fail")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(f".\\Screenshots\\test_verify_login_param_005_login_fail_{email}_{password}.png")
            actual_result = "login fail"

        if expected_result == actual_result:
            self.log.info("test_verify_login_param_005 is passed")
            assert True
        else:
            self.log.info("test_verify_login_param_005 is failed")
            assert False

        self.log.info("test_verify_login_param_005 is completed")



# command
# pytest -v -s -n auto --html=HTML_Reports/report.html --alluredir=allure-result