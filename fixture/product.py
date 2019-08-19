from model.product import Product


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
