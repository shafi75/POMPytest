import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
import sys
file_dir=os.path.dirname("..//POMProject")
sys.path.append(file_dir)
from Utilities import configreader
import time
import allure

@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):
    output=yield
    rep=output.get_result()
    setattr(item,"rep_"+rep.when,rep)
    return rep

@pytest.fixture()
def log_on_failure(request,get_browser):
    yield
    item=request.node
    driver=get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),name="error",attachment_type=AttachmentType.PNG)


@pytest.fixture(params=["chrome"],scope="function")
def get_browser(request):
    global driver
    if request.param=="chrome":
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # if request.param=="firefox":
    #     driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # if request.param=="edge":
    #     driver=webdriver.Firefox(executable_path=EdgeChromiumDriverManager().install())
    request.cls.driver=driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(configreader.readConfig("basicinfo","testurl"))
    yield driver
    driver.quit()
