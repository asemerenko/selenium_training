from selenium.webdriver.support.color import Color


def test_compare_product_info(app):
    link = app.product.get_product_link_from_main_page()
    product_from_main_page = app.product.get_product_from_main_page()
    product_from_product_page = app.product.get_product_from_product_page(link)
    # а) на главной странице и на странице товара совпадает текст названия товара
    assert product_from_main_page.name == product_from_product_page.name
    # б) на главной странице и на странице товара совпадают цены (обычная и акционная)
    assert product_from_main_page.regular_price_text == product_from_product_page.regular_price_text
    assert product_from_main_page.campaign_price_text == product_from_product_page.campaign_price_text
    # в) обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой, у которого в
    # RGBa представлении одинаковые значения для каналов R, G и B)
    regular_price_red_main_page = Color.from_string(product_from_main_page.regular_price_color).red
    regular_price_green_main_page = Color.from_string(product_from_main_page.regular_price_color).green
    regular_price_blue_main_page = Color.from_string(product_from_main_page.regular_price_color).blue
    assert ((product_from_main_page.regular_price_style == "line-through")
            and (regular_price_red_main_page == regular_price_green_main_page == regular_price_blue_main_page))
    regular_price_red_product_page = Color.from_string(product_from_product_page.regular_price_color).red
    regular_price_green_product_page = Color.from_string(product_from_product_page.regular_price_color).green
    regular_price_blue_product_page = Color.from_string(product_from_product_page.regular_price_color).blue
    assert ((product_from_product_page.regular_price_style == "line-through")
            and (regular_price_red_product_page == regular_price_green_product_page == regular_price_blue_product_page))
    # г) акционная жирная и красная (можно считать, что "красный" цвет это такой, у которого
    # в RGBa представлении каналы G и B имеют нулевые значения)
    campaign_price_green_main_page = Color.from_string(product_from_main_page.campaign_price_color).green
    campaign_price_blue_main_page = Color.from_string(product_from_main_page.campaign_price_color).blue
    assert ((int(product_from_main_page.campaign_price_style) > 600)
            and (campaign_price_green_main_page == campaign_price_blue_main_page == 0))
    campaign_price_green_product_page = Color.from_string(product_from_product_page.campaign_price_color).green
    campaign_price_blue_product_page = Color.from_string(product_from_product_page.campaign_price_color).blue
    assert ((int(product_from_product_page.campaign_price_style) > 600)
            and (campaign_price_green_product_page == campaign_price_blue_product_page == 0))
    # д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)
    assert product_from_main_page.campaign_price_height > product_from_main_page.regular_price_height
    assert product_from_product_page.campaign_price_height > product_from_product_page.regular_price_height
