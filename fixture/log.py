class LogHelper:

    def __init__(self, app):
        self.app = app

    def go_to_catalog_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//ul[@id='box-apps-menu']").find_element_by_link_text('Catalog').click()
        wd.find_element_by_id("content").find_element_by_link_text('Rubber Ducks').click()

    def find_products_links(self):
        wd = self.app.wd
        links = wd.find_elements_by_xpath("//table[@class='dataTable']//td/img/../a")
        links_list = []
        for l in links:
            links_list.append(l.get_attribute("href"))
        return links_list

    def click_link_see_log(self, links_list):
        wd = self.app.wd
        for link in links_list:
            wd.get(link)
            for l in wd.get_log("browser"):
                print(l)
