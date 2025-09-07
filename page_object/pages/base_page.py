from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, element):
        self.wait.until(
            expected_conditions.presence_of_element_located(element))
        return self.driver.find_element(*element)

    def click_to_element(self, element):
        self.wait.until(
            expected_conditions.element_to_be_clickable(element))
        element = self.driver.find_element(*element)
        ActionChains(self.driver).move_to_element(element).perform()
        ActionChains(self.driver).click(element).perform()

    def add_text_to_element(self, element, text):
        self.find_element_with_wait(element).send_keys(text)

    def get_text_to_element(self, element):
        return self.find_element_with_wait(element).text

    def not_find_element_on_page(self, element):
        return self.wait.until(
            expected_conditions.invisibility_of_element(element))