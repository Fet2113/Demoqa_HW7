
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_icon_exist(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()

    assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()


    # assert demo_qa_page.click_on_the_icon("#app>div>div>div.home-body>div>div.nth-child(1)")
   #  assert demo_qa_page.exist_icon("https://demoqa.com/elements")