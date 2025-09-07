from selenium.webdriver.common.by import By

class CreateRecipePageLocators:
    BUTTON_SWITCH_TO_CREATE_RECIPE_PAGE = (By.XPATH,
                             ".//*[text()='Создать рецепт']")
    INPUT_NAME_RECIPE = (By.XPATH,
                             ".//*[@class='styles_input__2Dg_j']//*[@class='styles_inputField__3eqTj']")
    INPUT_NAME_INGREDIENT = (By.XPATH,
                         ".//*[@class='styles_inputField__3eqTj styles_ingredientsInput__1zzql']")
    INGREDIENT_IN_DROP_DOWN_LIST = (By.XPATH,
                             ".//*[@class='styles_container__3ukwm']/div[1]")
    BUTTON_ADD_INGREDIENT = (By.XPATH,
                             ".//*[@class='styles_ingredientAdd__3fc32']")
    INPUT_WEIGHT_INGREDIENT = (By.XPATH,
                             ".//*[@class='styles_inputField__3eqTj styles_ingredientsAmountValue__2matT']")
    INPUT_COOKING_TIME = (By.XPATH,
                         ".//*[@class='styles_input__2Dg_j styles_ingredientsTimeInput__3oqdd']//*[@class='styles_inputField__3eqTj']")
    INPUT_ABOUT_RECIPE = (By.XPATH,
                             ".//*[@class='styles_textareaField__1wfhC']")
    INPUT_SELECT_FILE = (By.XPATH,
                             ".//*[@class='styles_fileInput__3HjP3']")
    BUTTON_CREATE_RECIPE = (By.XPATH,
                            ".//button[text()='Создать рецепт']")
    HEADER_NAME_OF_CREATED_RECIPE = (By.XPATH,
                                     ".//*[@class='styles_single-card__title__2QMPq']")