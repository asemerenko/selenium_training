import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



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

    def click_links_on_country_page(self, countries_links_list):
        wd = self.app.wd
        link = random.choice(countries_links_list)
        wd.get(link)
        links_target_blank = wd.find_elements_by_css_selector("#content form a[target='_blank']")
        for link in links_target_blank:
            original_window = wd.current_window_handle
            existing_windows = wd.window_handles
            new_list_windows = []
            link.click()
            wait = WebDriverWait(wd, 5)
            if wait.until(ec.new_window_is_opened(existing_windows)):
                new_list_windows = wd.window_handles
                new_list_windows.remove(original_window)
            new_window = new_list_windows[0]
            wd.switch_to.window(new_window)
            wd.close()
            wd.switch_to.window(original_window)
