def test_compare_product_info(app):
    link = app.product.get_product_link_from_main_page()
    product_from_main_page = app.product.get_product_from_main_page()
    print(product_from_main_page)
    print(link)
    prroduct_from_product_page = app.product.get_product_from_product_page(link)
    print(prroduct_from_product_page)
