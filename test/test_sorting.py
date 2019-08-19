def test_sorting_of_countries_and_geo_zones(app, start):
    countries = app.countries.get_countries_list_from_countries_page()
    app.countries.check_alphabetical_order(countries)
    links = app.countries.get_links_where_time_zone_not_null()
    for link in links:
        geo = app.countries.get_geo_from_country_edit_page(link)
        app.countries.check_alphabetical_order(geo)
    links_geo_zone = app.countries.get_links_from_geo_zones_page()
    for link_geo_zone in links_geo_zone:
        geo_zone = app.countries.get_geo_zone_from_edit_geo_zone_page(link_geo_zone)
        app.countries.check_alphabetical_order(geo_zone)
