from pages.base_page import BasePage
from components.components import WebElement
class Accordian(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/accordian"

        self.elementA = WebElement(driver, "#section1Content > p")
        self.elementB = WebElement(driver, "#section1Heading")
        self.first_element = WebElement(driver, "#section2Content > p:nth-child(1)")
        self.second_element = WebElement(driver, "#section2Content > p:nth-child(2)")
        self.third_element = WebElement(driver, "#section3Content > p")
        super().__init__(driver, self.base_url)
