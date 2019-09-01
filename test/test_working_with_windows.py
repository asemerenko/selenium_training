def test_links_opening_in_new_window(app, start):
    countries_links_list = app.window.get_countries_links()
    app.window.click_links_on_country_page(countries_links_list)
