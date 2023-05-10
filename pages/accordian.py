from pages.base_page import BasePage
from components.components import WebElement
class Accordian(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/accordian"
        super().__init__(driver, self.base_url)

        self.elementA = WebElement(driver, "#section1Content > p")
        self.elementB = WebElement(driver, "#section1Heading")
        self.first_elements = WebElement(driver, "#section2Content > p:nth-child(1)")
        self.second_elements = WebElement(driver, "#section2Content > p:nth-child(2)")
        self.third_elements = WebElement(driver, "#section3Content > p")

