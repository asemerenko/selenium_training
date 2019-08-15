def test_menu(app, start):
    wd = app.wd
    menu = app.menu.get_main_menu()
    for index in range(len(menu)):
        menu[index].click()
        assert wd.find_element_by_tag_name("h1")
        submenu = app.menu.get_submenu()
        if len(submenu) != 0:
            for ind in range(len(submenu)):
                submenu[ind].click()
                assert wd.find_element_by_tag_name("h1")
                submenu = app.menu.get_submenu()
        menu = app.menu.get_main_menu()
