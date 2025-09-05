from page_object.pages.create_account_page import CreateAccountPage


class TestCreateAccount:

    def test_create_account(self, driver):
        create_account = CreateAccountPage(driver)
        create_account.switch_to_create_account_page()
        assert create_account.fill_fields_of_registration_form_and_click_create_account_button() == True
