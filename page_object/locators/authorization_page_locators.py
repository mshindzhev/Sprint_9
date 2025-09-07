from selenium.webdriver.common.by import By

class AuthorizationPageLocators:
    INPUT_EMAIL = (By.XPATH,
                       ".//*[@name='email']")
    INPUT_PASSWORD = (By.XPATH,
                      ".//*[@name='password']")
    BUTTON_LOGIN = (By.XPATH,
                   ".//*[@class='style_button__1FFWl styles_button__1jD3X style_button_style_dark-blue__1cpq7']")
    BUTTON_LOGOUT = (By.XPATH,
                    ".//*[text()='Выход']")

