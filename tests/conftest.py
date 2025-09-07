import pytest
from selenium import webdriver

from page_object.pages.authorization_page import AuthorizationPage


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def authorization_user(driver):
    authorization_user = AuthorizationPage(driver)
    return authorization_user.authorization()