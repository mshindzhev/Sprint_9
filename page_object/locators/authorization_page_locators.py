from selenium.webdriver.common.by import By

class AuthorizationPageLocators:
    BUTTON_HISTORY_ORDERS = (By.XPATH,
                             ".//*[text()='Создать аккаунт']")
    OPENED_HISTORY_ORDERS = (By.XPATH,
                             ".//*[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9'][text()='История заказов']")