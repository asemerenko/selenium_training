def test_stiker(app):
    wd = app.wd
    wd.get("http://localhost/litecart/en/")
    products = wd.find_elements_by_css_selector(".product")
    for product in products:
        assert len(product.find_elements_by_css_selector(".sticker")) == 1
