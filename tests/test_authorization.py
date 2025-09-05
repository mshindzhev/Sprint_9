from page_object.pages.authorization_page import AuthorizationPage


class TestAuthorization:

    def test_authorization(self, driver):
        authorization_account = AuthorizationPage(driver)
        assert authorization_account.authorization() == True