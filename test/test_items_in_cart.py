def test_items_in_cart(app):
    n = 3
    quantity = 1
    product_list = app.cart.get_product_list()
    for ind in range(n):
        app.cart.add_item_to_cart(product_list, quantity)
    app.cart.del_items_from_cart()
