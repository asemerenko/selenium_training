def test_menu(app, start):
    wd = app.wd
    menu = wd.find_elements_by_css_selector('ul#box-apps-menu > li > a')
    len_menu = len(menu)
    for index in range(len_menu):
        menu[index].click()
        assert wd.find_element_by_tag_name("h1")
        submenu = wd.find_elements_by_css_selector('ul#box-apps-menu li.selected ul a')
        if len(submenu) != 0:
            for ind in range(len(submenu)):
                submenu[ind].click()
                assert wd.find_element_by_tag_name("h1")
                submenu = wd.find_elements_by_css_selector('ul#box-apps-menu li.selected ul a')
        menu = wd.find_elements_by_css_selector('ul#box-apps-menu > li > a')
