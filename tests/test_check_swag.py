from pages.swag_labs import SwagLabs

def test_check(browser):

    swaglabs_page = SwagLabs(browser)
    swaglabs_page.visit()
    assert swaglabs_page.exist_icon()
    assert swaglabs_page.exist_username()
    assert swaglabs_page.exist_password()