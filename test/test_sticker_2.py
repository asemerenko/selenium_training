from selenium.webdriver.common.by import By


def test_stiker_2(app):
    wd = app.wd
    wd.get("http://localhost/litecart/en/")
    products = wd.find_elements_by_css_selector(".product")
    for product in products:
        assert are_elements_present(product, By.CLASS_NAME, "sticker")


def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) == 1
