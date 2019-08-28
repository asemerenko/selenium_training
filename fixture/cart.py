from model.productchoice import ProductChoice
from random import randrange
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartHelper:

    def __init__(self, app):
        self.app = app

    def go_to_main_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/litecart/en/"):
            wd.get("http://localhost/litecart/en/")

    def get_product_list(self):
        wd = self.app.wd
        self.go_to_main_page()
        products = []
        pr_list = wd.find_elements_by_css_selector("#box-most-popular .product")
        for pr in pr_list:
            name = pr.find_element_by_class_name("name").text
            link = pr.find_element_by_class_name("link").get_attribute("href")
            products.append(ProductChoice(name=name, link=link))
        return products

    def add_item_to_cart(self, product_list):
        wd = self.app.wd
        index = randrange(len(product_list))
        wd.get(product_list[index].link)
        cart_quantity = wd.find_element_by_css_selector("#cart .quantity")
        old_quantity = cart_quantity.text
        if self.is_element_present(wd, By.NAME, "options[Size]"):
            Select(wd.find_element_by_name("options[Size]")).select_by_value('Small')
        self.fill_field_value("quantity", 1)
        wd.find_element_by_name("add_cart_product").click()
        wait = WebDriverWait(wd, 10)
        new_quantity = str(int(old_quantity) + 1)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart .quantity"), new_quantity))
        # product_list[index:index + 1] = []
        # return product_list

    def go_to_cart_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/litecart/en/checkout"):
            wd.find_element_by_link_text("Checkout »").click()

    def is_element_present(self, driver, *args):
        try:
            driver.find_element(*args)
            return True
        except NoSuchElementException:
            return False

    def fill_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
