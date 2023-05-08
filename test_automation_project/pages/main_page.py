from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_automation_project.base.base_class import Base


class Main_page(Base):

    # Variables
    url = 'https://www.citilink.ru/'

    # Locators
    laptop_catalog_button = "(//div[@class='app-catalog-xi606m e1ynzhvl0'])[1]"
    choose_city_button = "(//span[@class='elgmz660 e106ikdt0 css-1r38efs e1gjr6xo0'])[1]"
    button_city_close = "//button[@class='css-1vxpjfn e75ou2e0']"
    main_page_title = "(//h3[@class='e114sczy0 eml1k9j0 app-catalog-1nubtw6 e1gjr6xo0'])[1]"

    # Getters
    def get_city_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.choose_city_button))
        )

    def get_city_window_button(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_city_close))
        )

    def get_main_title(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.main_page_title))
        )

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.laptop_catalog_button))
        )

    # Methods
    def click_city_button(self):
        self.get_city_button().click()
        print('Click Choose City Button')

    def close_city_window(self):
        self.get_city_window_button().click()
        print('Click Close City Button')

    def click_catalog_button(self):
        self.driver.execute_script("window.scrollBy(0,450)", "")
        self.get_catalog_button().click()
        print('Click Laptop Button')

    # Actions

    # Выбор региона и переход на страницу каталога
    def main_page_action(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_city_button()
        self.close_city_window()
        assert self.get_main_title().text == 'Популярные категории'
        self.click_catalog_button()