from Pages.BasePage import BasePage
from Utilities import configreader

class CarBase(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def getCarTitle(self):
        return self.driver.find_element_by_xpath(configreader.readConfig("locators","carTitle_XPATH")).text

    def getCarNameAndPrices(self):
        carNames=self.driver.find_elements_by_xpath(configreader.readConfig("locators","carName_XPATH"))
        carPrices=self.driver.find_elements_by_xpath(configreader.readConfig("locators","carPrice_XPATH"))

        for i in range(len(carNames)):
            print(("Car name: "+carNames[i].text+"Car Price is: "+carPrices[i].text).encode('utf8'))
