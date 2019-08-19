class CountriesHelper:

    def __init__(self, app):
        self.app = app

    def open_countries_page(self):
        wd = self.app.wd
        if not ((wd.current_url == "http://localhost/litecart/admin/?app=countries&doc=countries")
                and (wd.find_element_by_tag_name("h1").text == 'Countries')):
            wd.find_element_by_link_text("Countries").click()

    def open_geo_zones_page(self):
        wd = self.app.wd
        if not ((wd.current_url == "http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
                and (wd.find_element_by_tag_name("h1").text == 'Geo Zones')):
            wd.find_element_by_link_text("Geo Zones").click()

    def get_countries_list_from_countries_page(self):
        wd = self.app.wd
        self.open_countries_page()
        rows = wd.find_element_by_name("countries_form").find_elements_by_class_name("row")
        countries = []
        for row in rows:
            countries.append(row.find_elements_by_tag_name("td")[4].text)
        return countries

    def get_links_where_time_zone_not_null(self):
        wd = self.app.wd
        self.open_countries_page()
        rows = wd.find_element_by_name("countries_form").find_elements_by_class_name("row")
        links = []
        for row in rows:
            if int(row.find_elements_by_tag_name("td")[5].text) > 0:
                links.append(row.find_elements_by_tag_name("td")[4].find_element_by_tag_name("a").get_attribute("href"))
        return links

    def get_geo_from_country_edit_page(self, link):
        wd = self.app.wd
        wd.get(link)
        rows_table = wd.find_element_by_id("table-zones").find_elements_by_tag_name("tr")
        rows_geo = rows_table[1:(len(rows_table) - 1)]
        geo = []
        for row_geo in rows_geo:
            geo.append(row_geo.find_elements_by_tag_name("td")[2].text)
        return geo

    def get_links_from_geo_zones_page(self):
        wd = self.app.wd
        self.open_geo_zones_page()
        row_table = wd.find_element_by_class_name("dataTable").find_elements_by_class_name("row")
        links = []
        for row in row_table:
            links.append(row.find_elements_by_tag_name("td")[2].find_element_by_tag_name("a").get_attribute("href"))
        return links

    def get_geo_zone_from_edit_geo_zone_page(self, link):
        wd = self.app.wd
        wd.get(link)
        rows_table = wd.find_element_by_id("table-zones").find_elements_by_tag_name("tr")
        rows_geo = rows_table[1:(len(rows_table) - 1)]
        geo = []
        for row_geo in rows_geo:
            select_geos = row_geo.find_elements_by_tag_name("td")[2].find_element_by_tag_name("select").\
                find_elements_by_tag_name("option")
            for select_geo in select_geos:
                if select_geo.is_selected():
                    geo.append(select_geo.text)
        return geo

    def check_alphabetical_order(self, list_for_verify):
        sorted_list = sorted(list_for_verify)
        len_list = len(list_for_verify)
        for index in range(len_list):
            assert list_for_verify[index] == sorted_list[index]
