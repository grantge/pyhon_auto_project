import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_automation_project.base.base_class import Base


class Product_page(Base):

    # Variables
    product_code = 'Код товара: 1884629'

    # Locators
    tab_product_about = "(//label[@class='app-catalog-1estdu7 e2u86g20'])[1]"

    product_purchase_code = "//span[@class='e1n0yuko0 e1o6fkkp0 e106ikdt0 app-catalog-2pygxp e1gjr6xo0']"
    product_button = "//button[@class='e11w80q30 e4uhfkv0 app-catalog-1c1fy1q e4mggex0']"
    continue_button = "//button[@class='e4uhfkv0 css-tugfqc e4mggex0']"
    basket_button = "//button[@class='e4uhfkv0 css-10je9jt e4mggex0']"

    # Getters
    def get_product_code(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.product_purchase_code))
        )

    def get_tab_about(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.tab_product_about))
        )

    def add_product_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.product_button))
        )

    def get_continue_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_button))
        )

    def get_basket_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.basket_button))
        )

    # Methods
    def click_tab_about(self):
        self.get_tab_about().click()
        print('Click Tab About')

    def click_add_product_button(self):
        self.add_product_button().click()
        print('Click Product Button')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click Continue Button')

    def click_basket_button(self):
        self.get_basket_button().click()
        # print('Click Product Basket Button')

    # Actions

    # Добавление товара и переход в корзину
    def product_page_action(self):
        assert self.product_code == self.get_product_code().text
        self.driver.execute_script("window.scrollBy(0,500)", "")
        self.click_tab_about()
        self.driver.execute_script("window.scrollBy(0, -500)", "")
        self.click_add_product_button()
        self.click_continue_button()
        time.sleep(10)
        self.click_add_product_button()
