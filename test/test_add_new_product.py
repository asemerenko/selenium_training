def test_add_new_product(app, start):
    app.product.go_to_add_new_product_page()
    name = app.product.create_product()
    app.product.check_product_has_been_added(name)
