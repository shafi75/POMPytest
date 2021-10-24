from Pages.BasePage import BasePage
from Utilities import configreader

class NewCarsPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def selectHyundayi(self):
        self.click("hyundayi_XPATH")

    def selectHonda(self):
        self.click("honda_XPATH")

    def selectToyota(self):
        self.click("toyota_XPATH")

    def selectBMW(self):
        self.click("bmw_XPATH")