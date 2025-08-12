# import allure
# import pytest
# import sys
# import os
#
# from utitlties.Excel_utilities import  Excel_utilities_class
#
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#
# from pageObjects.Login_Page import LoginPage_Class
# from utitlties.Logger import LoggerClass
# from utitlties.readconfigfile import ReadConfig
#
#
# @pytest.mark.usefixtures("setup")
# class Test_Login_excel_005:
#     log = LoggerClass.get_loggen()
#     login_url = ReadConfig.get_login_url()
#     driver = None
#     excel_file_path = r"D:\Batch Notes\Automation Testing may 2025\06. Credkart_Pytest_Revision\TestData\Test_data_File.xlsx"
#     sheet_name = "login_data"
#     @pytest.mark.smoke
#     @pytest.mark.regression
#     #@pytest.mark.dependency(depends=["test_verify_title_001"]) # here we have used the dependency
#     @pytest.mark.flaky(reruns=1, reruns_delay=1)
#     @allure.title("test_verify_login_excel_006")
#     @allure.severity(allure.severity_level.NORMAL)
#     @allure.description("Verify that user is able to login to the application")
#     def test_verify_login_excel_006(self):
#         self.log.info("test_verify_login_excel_006 is started")
#         self.lp = LoginPage_Class(self.driver)
#         self.log.info("Reading data from excel file")
#         self.count_rows = Excel_utilities_class.getRowCount(self.excel_file_path, self.sheet_name)
#         result_list=[]
#         for i in range(2, self.count_rows + 1):
#             self.log.info(f"Opening the login page-->{self.login_url}")
#             self.driver.get(self.login_url)
#             self.log.info(f"Reading data from row-->{i}")
#             email = Excel_utilities_class.read_data(self.excel_file_path, self.sheet_name, i, 1)
#             password = Excel_utilities_class.read_data(self.excel_file_path, self.sheet_name, i, 2)
#             expected_result = Excel_utilities_class.read_data(self.excel_file_path, self.sheet_name, i, 3)
#             self.log.info(f"Enter email-->{email}")
#             self.lp.Enter_email(email)
#             self.log.info(f"Enter password-->{password}")
#             self.lp.Enter_password(password)
#             self.log.info("Click login button")
#             self.lp.Click_login()
#             self.log.info("Verify login")
#             if  self.lp.Verify_menu() == "pass":
#                 self.log.info("login pass")
#                 self.log.info("Taking screenshot")
#                 self.driver.save_screenshot(f".\\Screenshots\\test_verify_login_param_005_login_pass_{email}_{password}.png")
#                 self.log.info("Click menu button")
#                 self.lp.Click_menu()
#                 self.log.info("Click logout button")
#                 self.lp.Click_logout()
#                 actual_result = "login pass"
#             else:
#                 self.log.info("login fail")
#                 self.log.info("Taking screenshot")
#                 self.driver.save_screenshot(f".\\Screenshots\\test_verify_login_param_005_login_fail_{email}_{password}.png")
#                 actual_result = "login fail"
#
#             Excel_utilities_class.write_data(self.excel_file_path, self.sheet_name, i, 4, actual_result)
#
#             if expected_result == actual_result:
#                 result_list.append("pass")
#                 test_status = "pass"
#             else:
#                 result_list.append("fail")
#                 test_status = "pass"
#             Excel_utilities_class.write_data(self.excel_file_path, self.sheet_name, i, 5, test_status)
#
#
#
#         if "fail" not in result_list:
#             self.log.info("test_verify_login_excel_006 is passed")
#             assert True
#         else:
#             self.log.info("test_verify_login_excel_006 is failed")
#             assert False
#         self.log.info("test_verify_login_excel_006 is completed")
#
#
# # command
# # pytest -v -s -n auto --html=HTML_Reports/report.html --alluredir=allure-results