def test_items_in_cart(app):
    n = 3
    product_list = app.cart.get_product_list()
    for ind in range(n):
        # product_list = \
        app.cart.add_item_to_cart(product_list)
    app.cart.go_to_cart_page()
