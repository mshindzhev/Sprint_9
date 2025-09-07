from selenium.webdriver.common.by import By

class CreateAccountPageLocators:
    BUTTON_SWITCH_TO_CREATE_ACCOUNT_PAGE = (By.XPATH,
                             ".//*[text()='Создать аккаунт']")
    INPUT_FIRST_NAME = (By.XPATH,
                             ".//*[@name='first_name']")
    INPUT_LAST_NAME = (By.XPATH,
                        ".//*[@name='last_name']")
    INPUT_USER_NAME = (By.XPATH,
                       ".//*[@name='username']")
    INPUT_EMAIL = (By.XPATH,
                       ".//*[@name='email']")
    INPUT_PASSWORD = (By.XPATH,
                   ".//*[@name='password']")
    BUTTON_CREATE_ACCOUNT = (By.XPATH,
                             ".//*[@class='style_button__1FFWl styles_button__146Sy style_button_style_dark-blue__1cpq7']")
