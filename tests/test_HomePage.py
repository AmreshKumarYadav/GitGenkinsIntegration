import time

import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        time.sleep(2)
        homepage.getName().send_keys(getData["firstname"])
        time.sleep(2)
        homepage.getEmail().send_keys(getData["lastname"])
        time.sleep(2)
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        time.sleep(2)

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text
        time.sleep(2)
        assert ("Success1" in alertText)
        # self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Test_1"))
    def getData(self, request):
        return request.param

