"""
More involved iOS tests, using UICatalog application.
"""
import time
import os
import random
import string
from appium import webdriver
import appium.webdriver.webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
import urllib3.request as urllib2
import json
from time import sleep


def test_create_project(driver: webdriver.webdriver.WebDriver):
    try:
        e = webdriver.find_element_by_xpath('//XCUIElementTypeApplication[@name="Blackout"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell')
        e.click()
        webdriver.find_element_by_xpath('//*[contains(@name, "house")]').click()
        webdriver.find_element_by_xpath('//*[contains(@name, "Effects")]').click()
        webdriver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="14"]').click()
        webdriver.find_element_by_xpath('//XCUIElementTypeButton[@name="Update"]').click()
        input('press enter...')
    except Exception as e:
        print('---> error: ', str(e))
    finally:
        d.save_screenshot('out.png')
        d.quit()

class BlackoutAppTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        self.driver = init_driver()
        self._values = []

    def tearDown(self):
        self.driver.quit()

    def test_find_element(self):
        element = self.driver.find_element_by_name('Fixture Controls')
        element.click()

if __name__ == "__main__":
    #suite = unittest.TestLoader().loadTestsFromTestCase(BlackoutAppTests)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    run_test()
