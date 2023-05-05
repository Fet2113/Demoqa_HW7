
from pages.demoqa import DemoQa

#from selenium.webdriver.common.by import By


def test_icon_exist(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.icon.exist()
    assert demo_qa_page.equal_url()


    #browser.get("https://demoqa.com/")
   # icon = browser.find_element(By.CSS_SELECTOR, "#app > header > a")

    #if icon is None:
       # print("Элемент не найден")
    #else:
       # print("Эдемент найден")