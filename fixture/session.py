class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("login").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@title='Logout']").click()
        wd.find_element_by_name("username")

    def ensure_logout(self):
        if self.is_logged_in() > 0:
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//a[@title='Logout']"))

    def is_logged_in_as(self, username):
        return self.get_logged_user() == 'You are now logged in as %s' % username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("div.notice.success").text

    def ensure_login(self, username, password):
        if self.is_logged_in() > 0:
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
