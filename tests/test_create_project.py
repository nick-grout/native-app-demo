"""
More involved iOS tests, using UICatalog application.
"""
from appium.webdriver.webdriver import WebDriver
import random
import time
import string


def random_characters(length: int = 5):
    def random_character():
        return random.choice(string.ascii_letters + string.digits)
    return ''.join([random_character() for i in range(length)])


"""
def test_access_project(driver: WebDriver):
    e = driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="Blackout"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell')
    e.click()
    driver.find_element_by_xpath('//*[contains(@name, "house")]').click()
    driver.find_element_by_xpath('//*[contains(@name, "Effects")]').click()
    driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="14"]').click()
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Update"]').click()
"""


def test_create_project(driver: WebDriver):
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="+ Create new"]').click()
    test_project_name = 'test-project-' + random_characters()
    driver.find_element_by_xpath('//XCUIElementTypeTextField').send_keys(test_project_name)
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Save"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="{}"]'.format(test_project_name)).click()
    time.sleep(2)
