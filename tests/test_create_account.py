import allure

from page_object.pages.create_account_page import CreateAccountPage


class TestCreateAccount:

    @allure.title("Создание нового пользователя")
    def test_create_account(self, driver):
        with allure.step("Проверить успешное создание аккаунта"):
            create_account = CreateAccountPage(driver)
            create_account.switch_to_create_account_page()
            assert create_account.create_account() == True
