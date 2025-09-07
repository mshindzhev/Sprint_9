import allure

import data
from page_object.locators.create_recipe_page_locators import CreateRecipePageLocators
from page_object.pages.base_page import BasePage


class CreateRecipePage(BasePage):

    @allure.step("Переключение на раздел создания рецепта")
    def switch_to_create_recipe_page(self):
        self.find_element_with_wait(CreateRecipePageLocators.BUTTON_SWITCH_TO_CREATE_RECIPE_PAGE)
        self.click_to_element(CreateRecipePageLocators.BUTTON_SWITCH_TO_CREATE_RECIPE_PAGE)
        self.find_element_with_wait(CreateRecipePageLocators.INPUT_NAME_RECIPE)

    @allure.step("Создание рецепта")
    def create_recipe(self):
        self.add_text_to_element(CreateRecipePageLocators.INPUT_NAME_RECIPE, data.NAME_RECIPE)
        self.add_text_to_element(CreateRecipePageLocators.INPUT_WEIGHT_INGREDIENT, data.WEIGHT_INGREDIENT)
        self.add_text_to_element(CreateRecipePageLocators.INPUT_NAME_INGREDIENT, data.NAME_INGREDIENT)
        self.find_element_with_wait(CreateRecipePageLocators.INGREDIENT_IN_DROP_DOWN_LIST)
        self.click_to_element(CreateRecipePageLocators.INGREDIENT_IN_DROP_DOWN_LIST)
        self.find_element_with_wait(CreateRecipePageLocators.BUTTON_ADD_INGREDIENT)
        self.click_to_element(CreateRecipePageLocators.BUTTON_ADD_INGREDIENT)
        self.add_text_to_element(CreateRecipePageLocators.INPUT_COOKING_TIME, data.COOKING_TIME)
        self.add_text_to_element(CreateRecipePageLocators.INPUT_ABOUT_RECIPE, data.ABOUT_RECIPE)
        self.add_text_to_element(CreateRecipePageLocators.INPUT_SELECT_FILE, f"{data.APP_DIR}/assets/test.jpeg")
        self.click_to_element(CreateRecipePageLocators.BUTTON_CREATE_RECIPE)
        self.find_element_with_wait(CreateRecipePageLocators.HEADER_NAME_OF_CREATED_RECIPE)

        if self.get_text_to_element(CreateRecipePageLocators.HEADER_NAME_OF_CREATED_RECIPE) == data.NAME_RECIPE:
            return True
        return False

