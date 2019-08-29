class WindowHelper:

    def __init__(self, app):
        self.app = app

    def go_to_countries_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/litecart/admin/?app=countries&doc=countries"
                and wd.find_element_by_tag_name("h1").text == "Countries"):
            wd.find_element_by_link_text("Countries").click()

    def get_countries_links(self):
        wd = self.app.wd
        self.go_to_countries_page()
        rows = wd.find_element_by_class_name("dataTable").find_elements_by_class_name("row")
        countries_links_list = []
        for row in rows:
            countries_links_list.append(row.find_elements_by_tag_name("td")[4].
                                        find_element_by_tag_name("a").get_attribute("href"))
        return countries_links_list
