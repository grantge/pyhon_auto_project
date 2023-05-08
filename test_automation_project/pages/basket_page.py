import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_automation_project.base.base_class import Base


class Basket_page(Base):

    # Variables
    page_basket_name = 'Корзина'

    # Locators
    page_basket_title = "//span[@class='e1ys5m360 e106ikdt0 css-1f8xctp e1gjr6xo0']"
    clear_basket_button = "//button[@class='e4uhfkv0 css-tugfqc e4mggex0']"
    return_button = "//a[@class='css-mvz5ce e1yhwzjb0']"

    # Getters
    def get_page_title(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.page_basket_title))
        )

    def get_clear_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.clear_basket_button))
        )

    def get_return_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.return_button))
        )

    # Methods
    def click_clear_button(self):
        self.get_clear_button().click()
        print('Basket Cleared')

    def click_return_button(self):
        self.get_return_button()
        print('Return to Main Page')

    # Actions

    # Добавление товара и переход в корзину
    def basket_page_action(self):
        assert self.page_basket_name == self.get_page_title().text
        time.sleep(5)
        self.driver.save_screenshot('screenie.png')
        self.click_clear_button()
        self.click_return_button()
