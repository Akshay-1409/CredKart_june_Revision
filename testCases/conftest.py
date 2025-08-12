import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")



@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Running tests on chrome browser")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Running tests on firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Running tests on edge browser")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("Running tests on chrome browser-headless")
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(options=options)
    else:
        print("Running tests on Firefox browser")
        driver = webdriver.Firefox()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(params =[

    ("credencejune01@credence.in", "Credence@123", "login pass"),
    ("credencejune01@credence.in1", "Credence@123", "login fail"),
    ("credencejune01@credence.in", "Credence@1231", "login fail"),
    ("credencejune01@credence.in1", "Credence@1231", "login fail")
])
def data_for_login(request):
    return request.param