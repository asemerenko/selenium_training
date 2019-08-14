from selenium import webdriver
from fixture.session import SessionHelper


class Application:
    def __init__(self, browser, config):
        if browser == "firefox-new":
            self.wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
        elif browser == "firefox-esr":
            self.wd = webdriver.Firefox(capabilities={"marionette": False},
                                        firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox ESR\\firefox.exe")
        elif browser == "firefox-nightly":
            self.wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Firefox Nightly\\firefox.exe")
        elif browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            self.wd = webdriver.Chrome(chrome_options=options)
        elif browser == "ie":
            self.wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        print(self.wd.capabilities)
        self.session = SessionHelper(self)
        self.wd.implicitly_wait(3)
        self.config = config
        self.base_url = config['web']['baseUrl']

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
