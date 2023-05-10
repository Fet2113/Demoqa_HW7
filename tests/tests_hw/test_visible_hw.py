from pages.demoqa import DemoQa
from pages.accordian import Accordian
import  time
def test_visible_elementA(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    assert accordian_page.elementA.visible()
    accordian_page.elementA.click()
    time.sleep(2)
    assert not accordian_page.elementA.visible()
def test_click_elementB(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    assert accordian_page.elementB.click()
    time.sleep(2)
def test_visible_accordian_default(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    assert accordian_page.first_elements.visible()
    assert not accordian_page.first_elements.visible()
    assert accordian_page.second_elements.visible()
    assert not accordian_page.second_elements.visible()
    assert accordian_page.third_elements.visible()
    assert not accordian_page.third_elements.visible()
