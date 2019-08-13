def test_login(app):
    if app.session.is_logged_in() > 0:
        app.session.logout()
    app.session.login("admin", "admin")
    assert app.session.is_logged_in_as("admin")
