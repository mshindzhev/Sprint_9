import allure

from page_object.pages.authorization_page import AuthorizationPage


class TestAuthorization:

    @allure.title("Авторизация существующим пользователем")
    def test_authorization(self, driver):
        with allure.step("Проверить успешную авторизацию"):
            authorization_account = AuthorizationPage(driver)
            assert authorization_account.authorization() == True