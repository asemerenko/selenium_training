import random
import string
from selenium.webdriver.support.ui import Select
from model.user import User


class AccountHelper:

    def __init__(self, app):
        self.app = app

    def captcha_off(self):
        wd = self.app.wd
        wd.find_element_by_link_text('Settings').click()
        wd.find_element_by_link_text('Security').click()
        rows = wd.find_elements_by_class_name('row')
        for row in rows:
            td_list = row.find_elements_by_tag_name('td')
            if td_list[0].text == 'CAPTCHA':
                if td_list[1].text == 'True':
                    link = td_list[2].find_element_by_tag_name('a').get_attribute("href")
                    wd.get(link)
                    wd.find_element_by_css_selector("input[type='radio'][value='0']").click()
                    wd.find_element_by_name("save").click()
                    print('CAPTCHA_OFF')
                elif td_list[1].text == 'False':
                    print('CAPTCHA_OFF')

    def go_to_main_page(self):
        wd = self.app.wd
        link = 'http://localhost/litecart/en/'
        if not (wd.current_url == link):
            wd.get(link)

    def find_link_for_create_account(self):
        wd = self.app.wd
        self.go_to_main_page()
        return wd.find_element_by_link_text('New customers click here').get_attribute("href")

    def go_to_create_account_page(self, link):
        wd = self.app.wd
        if not (wd.current_url == link and wd.find_element_by_tag("h1").text == 'Create Account'):
            wd.get(link)

    def random_email(self, email_prefix, random_maxlen):
        return email_prefix + '+' + ''.join([random.choice(string.digits)
                                             for i in range(random_maxlen)]) + '@gmail.com'

    def random_string(self, prefix, maxlen):
        return prefix + ''.join([random.choice(string.digits) for i in range(maxlen)])

    def create_account(self):
        wd = self.app.wd
        email = self.random_email("test", 5)
        password = self.random_string("password", 5)
        firstname = self.random_string("firstname", 5)
        lastname = self.random_string("lastname", 5)
        self.fill_contact_field_value("tax_id", self.random_string("tax_id", 3))
        self.fill_contact_field_value("company", self.random_string("company", 5))
        self.fill_contact_field_value("firstname", firstname)
        self.fill_contact_field_value("lastname", lastname)
        self.fill_contact_field_value("address1", self.random_string("address1", 10))
        self.fill_contact_field_value("address2", self.random_string("address2", 10))
        self.fill_contact_field_value("postcode", self.random_string("", 5))
        self.fill_contact_field_value("city", self.random_string("city", 5))
        Select(wd.find_element_by_name("country_code")).select_by_visible_text('Ukraine')
        self.fill_contact_field_value("email", email)
        self.fill_contact_field_value("phone", "+380974444444")
        wd.find_element_by_name("newsletter").click()
        self.fill_contact_field_value("password", password)
        self.fill_contact_field_value("confirmed_password", password)
        wd.find_element_by_name("create_account").click()
        return User(email=email, password=password, firstname=firstname, lastname=lastname)

    def fill_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def account_has_been_created(self):
        wd = self.app.wd
        assert wd.find_element_by_css_selector(".notice.success").text == 'Your customer account has been created.'

    def logout(self):
        wd = self.app.wd
        links = wd.find_elements_by_css_selector("#navigation a")
        for link in links:
            if link.text == 'Logout':
                wd.get(link.get_attribute("href"))
        assert wd.find_element_by_css_selector(".notice.success").text == 'You are now logged out.'

    def login(self, user):
        wd = self.app.wd
        self.go_to_main_page()
        self.fill_contact_field_value("email", user.email)
        self.fill_contact_field_value("password", user.password)
        wd.find_element_by_name("login").click()
        string_text = "You are now logged in as " + user.firstname + " " + user.lastname + "."
        assert wd.find_element_by_css_selector(".notice.success").text == string_text
