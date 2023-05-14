from pages.demoqa import DemoQa
from pages.accordian import Accordian
import  time
def test_visible_accordian(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    assert accordian_page.elementA.visible()
    accordian_page.elementA.click()
    time.sleep(2)

def test_click_elementB(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    accordian_page.elementB.click()
    time.sleep(2)
    assert not accordian_page.elementB.visible()
def test_visible_accordian_default(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    assert accordian_page.first_element.visible()
    assert not accordian_page.first_element.visible()
    assert accordian_page.second_element.visible()
    assert not accordian_page.second_element.visible()
    assert accordian_page.third_element.visible()
    assert not accordian_page.third_element.visible()
