from pages.text_page import TextBox
import time
def test_clear(browser):
    textbox_page = TextBox(browser)
    textbox_page.visit()
    textbox_page.full_name.send_keys("Vovk")
    time.sleep(2)
    textbox_page.full_name.clear()
    time.sleep(2)
    assert textbox_page.full_name.get_text() == ""