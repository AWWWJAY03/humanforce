import logging
from datetime import datetime
import pytest
from selenium import webdriver
import os

from pages.admin import AdminPage
from pages.home import HomePage
from pages.humanforce import HumanforcePage
from pages.login import LoginPage

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa")
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture()
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="class")
def driver(request):
    browser = request.config.getoption("--browser").lower()
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "ie" or browser == "edge":
        driver = webdriver.Edge()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        chrome_options = webdriver.ChromeOptions()
        if browser == "headless": chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver

    #Save Screenshots
    os.makedirs('reports/screenshots', exist_ok=True)
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.png"
    filepath = os.path.join('reports', 'screenshots', filename)
    driver.save_screenshot(filepath)
    logging.info(f"Screenshot saved to {filepath}")
    driver.quit()

@pytest.fixture()
def url(env):
    if env == "prod":
        return "https://prdtestchallenge.humanforce.io"
    elif env == "dev":
        return "https://devtestchallenge.humanforce.io"
    else:
        return "https://qatestchallenge.humanforce.io"

@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture()
def home_page(driver):
    return HomePage(driver)

@pytest.fixture()
def admin_page(driver):
    return AdminPage(driver)

@pytest.fixture()
def humanfoce_page(driver):
    return HumanforcePage(driver)
