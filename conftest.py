import os

import pytest
from selenium import webdriver

from page_object.pages.authorization_page import AuthorizationPage


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')

    # Проверяем, запущены ли мы в контейнере с Selenoid
    if os.environ.get('SELENOID_ENABLED', 'false') == 'true':
        # Используем Remote WebDriver для Selenoid
        driver = webdriver.Remote(
            command_executor='http://selenoid:4444/wd/hub',
            options=options
        )
    else:
        # Локальный ChromeDriver (для разработки)
        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def authorization_user(driver):
    authorization_user = AuthorizationPage(driver)
    return authorization_user.authorization()