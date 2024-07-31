import unittest

from Python_Training.testingSamsung.pages.homePage import homePage
from Python_Training.testingSamsung.tests.globalSamsung import urlSamsung
from Python_Training.testingSamsung.tests.samsungSelenium import samsungSelenium


class s24_Test(unittest.TestCase):
    def test_s24(self):
        base = samsungSelenium()

        driver = base.selenium_start(urlSamsung)
        home_Page = homePage(driver)

        home_Page.search_Function()

        print("Test End")
