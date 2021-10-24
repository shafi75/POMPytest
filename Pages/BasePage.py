from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from Utilities import configreader
import logging
from Utilities.LogUtil import Logger

log=Logger(__name__,logging.INFO)
class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def click(self,locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configreader.readConfig("locators",locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css(configreader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configreader.readConfig("locators", locator)).click()
        log.logger.info("Clicking on the element"+str(locator))

    def type(self,locator,value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configreader.readConfig("locators",locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css(configreader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configreader.readConfig("locators", locator)).send_keys(value)
        log.logger.info("Enter the value in the element: " + str(locator)+" and the value is: "+value)

    def select(self,locator,value):
        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown=self.driver.find_element_by_xpath(configreader.readConfig("locators",locator))
        elif str(locator).endswith("_CSS"):
            dropdown=self.driver.find_element_by_css(configreader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            dropdown=self.driver.find_element_by_id(configreader.readConfig("locators", locator))

        select=Select(dropdown)
        select.select_by_visible_text(value)
        log.logger.info("Select the value for the dropdown: " + str(locator) + " and the value is: " + value)

    def move_to(self,locator):
        if str(locator).endswith("_XPATH"):
            element=self.driver.find_element_by_xpath(configreader.readConfig("locators",locator))
        elif str(locator).endswith("_CSS"):
            element=self.driver.find_element_by_css(configreader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            element=self.driver.find_element_by_id(configreader.readConfig("locators", locator))

        action=ActionChains(self.driver)
        action.move_to_element(element).perform()
        log.logger.info("Move to the element: " + str(locator))

