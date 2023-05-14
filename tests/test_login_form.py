from pages.form_page import FormPage
import time
from selenium.webdriver.common.keys import Keys

def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys("tester")
    form_page.last_name.send_keys("testerovich")
    form_page.user_email.send_keys("test@ttt.tt")
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys("9992223344")
    form_page.hobbies.click_force()
    form_page.current_address.send_keys("Mars")

    form_page.City.scroll_to_element()

    form_page.City.click()
    form_page.state_and_City.click()
    # form_page.state_and_City.send_keys(Keys.ENTER)

    time.sleep(2)

    # form_page.state_and_City.send_keys("NCR")
    # form_page.state_and_City.send_keys(Keys.ENTER)

    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()
    time.sleep(2)


