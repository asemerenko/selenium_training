def test_links_opening_in_new_window(app, start):
    countries_links_list = app.window.get_countries_links()
