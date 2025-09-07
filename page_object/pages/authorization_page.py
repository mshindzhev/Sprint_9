import allure

import data
from page_object.locators.authorization_page_locators import AuthorizationPageLocators
from page_object.pages.base_page import BasePage


class AuthorizationPage(BasePage):

    @allure.step("Авторизация")
    def authorization(self):
        self.go_to_url(f"{data.BASE_URL}{data.SIGNIN_URL}")
        self.find_element_with_wait(AuthorizationPageLocators.INPUT_EMAIL)
        self.add_text_to_element(AuthorizationPageLocators.INPUT_EMAIL, data.EMAIL)
        self.add_text_to_element(AuthorizationPageLocators.INPUT_PASSWORD, data.PASSWORD)
        self.click_to_element(AuthorizationPageLocators.BUTTON_LOGIN)

        if self.find_element_with_wait(AuthorizationPageLocators.BUTTON_LOGOUT):
            return True
        return False


