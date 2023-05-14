from pages.text_page import TextBox
import time
def test_placeholder(browser):
    textbox_page = TextBox(browser)
    textbox_page.visit()
    assert textbox_page.full_name.get_dom_attribute("placeholder") == "Full Name"
    time.sleep(2)
