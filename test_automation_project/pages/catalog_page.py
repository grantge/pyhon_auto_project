from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_automation_project.base.base_class import Base


class Catalog_page(Base):

    # Variables
    product_name = 'Ноутбук Apple MacBook Pro A2485, 16.2", Apple M1 Max 10 core, 10-ядерный, 64ГБ 512ГБ, серый космос'

    # Locators
    filter_brand_checkbox = "//input[@id='apple']"
    filter_ram_extend = "(//button[@data-meta-name='FilterGroup__show-all'])[7]"
    filter_ram_checkbox = "// input[@id='19967_364d1gb']"
    catalog_product = "(//a[@class='app-catalog-9gnskf e1259i3g0'])[1]"

    # Getters
    def get_brand_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.filter_brand_checkbox))
        )

    def extend_ram_filter(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.filter_ram_extend))
        )

    def get_ram_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.filter_ram_checkbox))
        )

    def get_catalog_product(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_product))
        )

    # Methods
    def click_brand_checkbox(self):
        self.driver.execute_script("window.scrollBy(0,1250)", "")
        self.get_brand_checkbox().click()
        print('Filter Products - Brand')

    def open_ram_filter(self):
        self.driver.execute_script("window.scrollBy(0,1550)", "")
        self.extend_ram_filter().click()
        print('Filter Products Extend')

    def click_ram_checkbox(self):
        self.get_ram_checkbox().click()
        print('Filter Products - RAM')

    def click_catalog_product(self):
        self.get_catalog_product().click()
        print('Click Product')

    # Actions

    # Выбор товара и переход на страницу просмотра товара
    def catalog_page_action(self):
        self.click_brand_checkbox()
        self.open_ram_filter()
        self.click_ram_checkbox()
        self.driver.execute_script("window.scrollBy(0,-3000)", "")
        assert self.product_name == self.get_catalog_product().text
        self.click_catalog_product()