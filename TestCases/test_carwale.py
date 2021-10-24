import pytest
from Pages.HomePage import HomePage
from Pages.carBase import CarBase
from TestCases.BaseTest import BaseTest
import logging
import time
from Utilities.LogUtil import Logger
from Utilities import dataProvider as dp

log=Logger(__name__,logging.INFO)

class Test_CarWale(BaseTest):
    @pytest.mark.sanity
    def test_carwale(self):
        log.logger.info("******************Inside New Car Test**************")
        home=HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(5)

    @pytest.mark.functional
    @pytest.mark.parametrize("carModel,carTitle",dp.get_data("..//Excel//testdata.xlsx","NewCarsPage"))
    def test_SelectCars(self,carModel,carTitle):
        log.logger.info("******************Inside Select Car Test**************")
        home = HomePage(self.driver)
        car= CarBase(self.driver)
        print(("The car model is : "+carModel).encode('utf8'))
        if carModel=="BMW":
            home.gotoNewCars().selectBMW()
            actual_title=car.getCarTitle()
            print(("The actual title is: "+actual_title).encode('utf8'))
            assert actual_title==carTitle,"Not Correct Page, Title does not matching"
            car.getCarNameAndPrices()
        elif carModel=="Hyundayi":
            home.gotoNewCars().selectHyundayi()
            actual_title = car.getCarTitle()
            print(("The actual title is: "+actual_title).encode('utf8'))
            assert actual_title == carTitle, "Not Correct Page, Title does not matching"
            car.getCarNameAndPrices()
        elif carModel=="Honda":
            home.gotoNewCars().selectHonda()
            actual_title = car.getCarTitle()
            print(("The actual title is: "+actual_title).encode('utf8'))
            assert actual_title == carTitle, "Not Correct Page, Title does not matching"
            car.getCarNameAndPrices()
        elif carModel=="Toyota":
            home.gotoNewCars().selectToyota()
            actual_title = car.getCarTitle()
            print(("The actual title is: "+actual_title).encode('utf8'))
            assert actual_title == carTitle, "Not Correct Page, Title does not matching"
            car.getCarNameAndPrices()
        time.sleep(5)



