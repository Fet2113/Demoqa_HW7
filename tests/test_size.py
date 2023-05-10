from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time
def test_set_window_dize(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert browser.set_window_size(width=1000, height=300)
    time.sleep(2)
    assert browser.set_window_size(width=1000, height=1000)
