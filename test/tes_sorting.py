def test_sorting_of_countries_and_geofences(app, start):
    wd = app.wd
    wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    rows = wd.find_element_by_name("countries_form").find_elements_by_class_name("row")
    countries = []
    links = []
    for row in rows:
        countries.append(row.find_elements_by_tag_name("td")[4].text)
        if int(row.find_elements_by_tag_name("td")[5].text) > 0:
            links.append(row.find_elements_by_tag_name("td")[4].find_element_by_tag_name("a").get_attribute("href"))
    check_alphabetical_order(countries)
    for link in links:
        wd.get(link)
        rows_table = wd.find_element_by_id("table-zones").find_elements_by_tag_name("tr")
        rows_geo = rows_table[1:(len(rows_table)-1)]
        geo = []
        for row_geo in rows_geo:
            geo.append(row_geo.find_elements_by_tag_name("td")[2].text)
        check_alphabetical_order(geo)
    wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")


def check_alphabetical_order(list_for_check):
    sorted_list = sorted(list_for_check)
    len_list = len(list_for_check)
    for index in range(len_list):
        assert list_for_check[index] == sorted_list[index]
