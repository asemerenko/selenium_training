def test_add_new_product(app, start):
    app.product.go_to_add_new_product_page()
    app.product.create_product()
