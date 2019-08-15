class MenuHelper:

    def __init__(self, app):
        self.app = app

    def get_main_menu(self):
        wd = self.app.wd
        return wd.find_elements_by_css_selector('ul#box-apps-menu > li > a')

    def get_submenu(self):
        wd = self.app.wd
        return wd.find_elements_by_css_selector('ul#box-apps-menu li.selected ul a')
