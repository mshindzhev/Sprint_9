import allure

from page_object.pages.create_recipe_page import CreateRecipePage


class TestCreateRecipe:

    @allure.title("Создание рецепта")
    def test_create_recipe(self, driver, authorization_user):
        with allure.step("Проверить успешное создание рецепта"):
            create_recipe = CreateRecipePage(driver)
            create_recipe.switch_to_create_recipe_page()
            assert create_recipe.create_recipe() == True