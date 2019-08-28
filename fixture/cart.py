from model.productchoice import ProductChoice
from random import randrange
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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

    def add_item_to_cart(self, product_list, q):
        wd = self.app.wd
        index = randrange(len(product_list))
        wd.get(product_list[index].link)
        cart_quantity = wd.find_element_by_css_selector("#cart .quantity")
        old_quantity = cart_quantity.text
        if is_element_present(wd, By.NAME, "options[Size]"):
            Select(wd.find_element_by_name("options[Size]")).select_by_value('Small')
        self.fill_field_value("quantity", q)
        wd.find_element_by_name("add_cart_product").click()
        new_quantity = str(int(old_quantity) + q)
        wait = WebDriverWait(wd, 5)
        wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart .quantity"), new_quantity))

    def del_items_from_cart(self):
        wd = self.app.wd
        self.go_to_cart_page()
        item_list = wd.find_elements_by_css_selector("[name='cart_form']")
        for item in range(len(item_list)):
            table = wd.find_element_by_css_selector(".dataTable")
            wd.find_element_by_css_selector("[name='cart_form']").find_element_by_name("remove_cart_item").click()
            wait = WebDriverWait(wd, 5)
            wait.until(ec.staleness_of(table))
        assert wd.find_element_by_css_selector("#checkout-cart-wrapper em").text == "There are no items in your cart."

    def go_to_cart_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/litecart/en/checkout"):
            wd.find_element_by_link_text("Checkout »").click()

    def fill_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False
