from selenium.webdriver.common.by import By


class LoginPageLocator:

    username_ele = (By.ID, 'username')
    password_ele = (By.ID, 'password')
    code_ele = (By.ID, 'validateCode')
    click_button = (By.XPATH, '//*[@class="btnLogin"]')
