import configparser
import os
from selenium import webdriver

config = configparser.ConfigParser()

#Get absolute path to config.ini
from pathlib import Path
base_dir = Path(__file__).resolve().parent.parent
config_path = base_dir / "Configurations" / "config.ini"

config.read(config_path)


class Readconfig:

    @staticmethod
    def get_email():
        email = config.get("login data", "email")
        return email


    @staticmethod
    def get_password():
        password =config.get("login data", "password")
        return password

    @staticmethod
    def get_login_url():
        login_url = config.get("Application URL", "login_url")
        return login_url


    @staticmethod
    def get_registration_url():
        registration_url = config.get("Application URL", "registration_url")
        return registration_url



