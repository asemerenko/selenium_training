from model.product import Product
import random
import string
from selenium.webdriver.support.ui import Select
import os.path


class ProductHelper:

    def __init__(self, app):
        self.app = app

    def go_to_main_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/litecart/en/"):
            wd.get("http://localhost/litecart/en/")

    def get_product_from_main_page(self):
        product_info = self.get_first_product_info_from_main_page()
        name = product_info.find_element_by_class_name("name").text
        regular_price = product_info.find_element_by_class_name("regular-price")
        regular_price_text = regular_price.text
        regular_price_color = regular_price.value_of_css_property("color")
        regular_price_height = regular_price.size['height']
        if (self.app.browser == "firefox-new") or (self.app.browser == "ie"):
            regular_price_style = regular_price.value_of_css_property("text-decoration")
        elif self.app.browser == "chrome":
            regular_price_style = regular_price.value_of_css_property("text-decoration-line")
        else:
            regular_price_style = regular_price.value_of_css_property("text-decoration")
        campaign_price = product_info.find_element_by_class_name("campaign-price")
        campaign_price_text = campaign_price.text
        campaign_price_color = campaign_price.value_of_css_property("color")
        campaign_price_height = campaign_price.size['height']
        campaign_price_style = campaign_price.value_of_css_property("font-weight")
        return Product(name=name, regular_price_text=regular_price_text, regular_price_color=regular_price_color,
                       regular_price_height=regular_price_height, regular_price_style=regular_price_style,
                       campaign_price_text=campaign_price_text, campaign_price_color=campaign_price_color,
                       campaign_price_height=campaign_price_height, campaign_price_style=campaign_price_style)

    def get_product_link_from_main_page(self):
        product_info = self.get_first_product_info_from_main_page()
        return product_info.find_element_by_css_selector("a.link").get_attribute("href")

    def get_first_product_info_from_main_page(self):
        wd = self.app.wd
        self.go_to_main_page()
        products_list = wd.find_element_by_id("box-campaigns").find_elements_by_class_name("products")
        return products_list[0].find_element_by_class_name("product")

    def get_product_from_product_page(self, link):
        wd = self.app.wd
        wd.get(link)
        product_info = wd.find_element_by_id("box-product")
        name = product_info.find_element_by_tag_name("h1").text
        regular_price = product_info.find_element_by_class_name("regular-price")
        regular_price_text = regular_price.text
        regular_price_color = regular_price.value_of_css_property("color")
        regular_price_height = regular_price.size['height']
        if (self.app.browser == "firefox-new") or (self.app.browser == "ie"):
            regular_price_style = regular_price.value_of_css_property("text-decoration")
        elif self.app.browser == "chrome":
            regular_price_style = regular_price.value_of_css_property("text-decoration-line")
        else:
            regular_price_style = regular_price.value_of_css_property("text-decoration")
        campaign_price = product_info.find_element_by_class_name("campaign-price")
        campaign_price_text = campaign_price.text
        campaign_price_color = campaign_price.value_of_css_property("color")
        campaign_price_height = campaign_price.size['height']
        campaign_price_style = campaign_price.value_of_css_property("font-weight")
        return Product(name=name, regular_price_text=regular_price_text, regular_price_color=regular_price_color,
                       regular_price_height=regular_price_height, regular_price_style=regular_price_style,
                       campaign_price_text=campaign_price_text, campaign_price_color=campaign_price_color,
                       campaign_price_height=campaign_price_height, campaign_price_style=campaign_price_style)

    def go_to_add_new_product_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//ul[@id='box-apps-menu']").find_element_by_link_text('Catalog').click()
        wd.find_element_by_id("content").find_element_by_link_text('Rubber Ducks').click()
        wd.find_element_by_id("content").find_element_by_link_text('Add New Product').click()

    def create_product(self):
        wd = self.app.wd
        name = self.random_string("Mustachioed_Duck", 3)
        # General
        if wd.find_element_by_css_selector(".tabs li.active a").text != 'General':
            wd.find_element_by_class_name("tabs").find_element_by_link_text('General').click()
        general = wd.find_element_by_id("tab-general")
        general.find_element_by_css_selector("input[type='radio'][value='1']").click()
        self.fill_contact_field_value(general, "name[en]", name)
        self.fill_contact_field_value(general, "code", self.random_string("rd", 3))
        Select(general.find_element_by_name("default_category_id")).select_by_visible_text('Rubber Ducks')
        self.fill_contact_field_value(general, "quantity", "30")
        Select(general.find_element_by_name("sold_out_status_id")).select_by_visible_text('Temporary sold out')
        path = self.img_path()
        general.find_element_by_name("new_images[]").send_keys(path)
        general.find_element_by_name("date_valid_from").send_keys("04042004")
        general.find_element_by_name("date_valid_to").send_keys("04042005")
        # Information
        if wd.find_element_by_css_selector(".tabs li.active a").text != 'Information':
            wd.find_element_by_class_name("tabs").find_element_by_link_text('Information').click()
        information = wd.find_element_by_id("tab-information")
        Select(information.find_element_by_name("manufacturer_id")).select_by_visible_text("ACME Corp.")
        self.fill_contact_field_value(information, "short_description[en]", self.random_string("short_description", 6))
        information.find_element_by_css_selector(".trumbowyg-editor").click()
        information.find_element_by_css_selector(".trumbowyg-editor").send_keys(self.random_string("description", 6))
        # Prices
        if wd.find_element_by_css_selector(".tabs li.active a").text != 'Prices':
            wd.find_element_by_class_name("tabs").find_element_by_link_text('Prices').click()
        prices = wd.find_element_by_id("tab-prices")
        self.fill_contact_field_value(prices, "purchase_price", 10)
        Select(prices.find_element_by_name("purchase_price_currency_code")).select_by_visible_text("US Dollars")
        self.fill_contact_field_value(prices, "prices[USD]", 20)
        self.fill_contact_field_value(prices, "prices[EUR]", 15)
        wd.find_element_by_id("content").find_element_by_name("save").click()
        return name

    def fill_contact_field_value(self, tab, field_name, text):
        if text is not None:
            tab.find_element_by_name(field_name).click()
            tab.find_element_by_name(field_name).clear()
            tab.find_element_by_name(field_name).send_keys(text)

    def random_string(self, prefix, maxlen):
        return prefix + ''.join([random.choice(string.digits) for i in range(maxlen)])

    def img_path(self):
        f = "img\\mustachioed-duck.png"
        file = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f))
        return file

    def check_product_has_been_added(self, name):
        wd = self.app.wd
        wd.find_element_by_xpath("//ul[@id='box-apps-menu']").find_element_by_link_text('Catalog').click()
        wd.find_element_by_id("content").find_element_by_link_text("Rubber Ducks").click()
        assert wd.find_element_by_class_name("dataTable").find_element_by_link_text(name)
