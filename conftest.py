from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver

from page_object.pages.authorization_page import AuthorizationPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Remote(
        command_executor='http://selenoid:4444/wd/hub',
        options=options
    )

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def authorization_user(driver):
    authorization_user = AuthorizationPage(driver)
    return authorization_user.authorization()