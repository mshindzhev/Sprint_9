import data
import helpers
from page_object.locators.authorization_page_locators import AuthorizationPageLocators
from page_object.locators.create_account_page_locators import CreateAccountPageLocators
from page_object.pages.base_page import BasePage


class CreateAccountPage(BasePage):

    def switch_to_create_account_page(self):
        self.go_to_url(f"{data.BASE_URL}{data.SIGNIN_URL}")
        self.not_find_element_on_page(CreateAccountPageLocators.INPUT_FIRST_NAME)
        self.find_element_with_wait(CreateAccountPageLocators.BUTTON_SWITCH_TO_CREATE_ACCOUNT_PAGE)
        self.click_to_element(CreateAccountPageLocators.BUTTON_SWITCH_TO_CREATE_ACCOUNT_PAGE)
        self.find_element_with_wait(CreateAccountPageLocators.INPUT_FIRST_NAME)

    def fill_fields_of_registration_form_and_click_create_account_button(self):
        self.add_text_to_element(CreateAccountPageLocators.INPUT_FIRST_NAME, helpers.generate_random_string())
        self.add_text_to_element(CreateAccountPageLocators.INPUT_LAST_NAME, helpers.generate_random_string())
        self.add_text_to_element(CreateAccountPageLocators.INPUT_USER_NAME, helpers.generate_random_string())
        self.add_text_to_element(CreateAccountPageLocators.INPUT_EMAIL, f"{helpers.generate_random_string()}@mail.ru")
        self.add_text_to_element(CreateAccountPageLocators.INPUT_PASSWORD, helpers.generate_random_string())
        self.click_to_element(CreateAccountPageLocators.BUTTON_CREATE_ACCOUNT)
        return self.find_element_with_wait(AuthorizationPageLocators.INPUT_EMAIL)


