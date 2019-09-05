def test_get_log(app, start):
    app.log.go_to_catalog_page()
    links = app.log.find_products_links()
    app.log.click_link_see_log(links)
