import time
from selenium import webdriver

from test_automation_project.pages.main_page import Main_page
from test_automation_project.pages.catalog_page import Catalog_page
from test_automation_project.pages.product_page import Product_page
from test_automation_project.pages.basket_page import Basket_page


def test_main_page():
    print('Test Started')
    driver = webdriver.Firefox()

    main = Main_page(driver)
    main.main_page_action()

    catalog = Catalog_page(driver)
    catalog.catalog_page_action()

    product = Product_page(driver)
    product.product_page_action()

    basket = Basket_page(driver)
    basket.basket_page_action()

    time.sleep(5)
    driver.close()

