def test_captcha(app, start):
    app.account.captcha_off()


def test_new_account(app):
    link = app.account.find_link_for_create_account()
    app.account.go_to_create_account_page(link)
    user = app.account.create_account()
    app.account.account_has_been_created()
    app.account.logout()
    app.account.login(user)
    app.account.logout()
