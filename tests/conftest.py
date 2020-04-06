import pytest
from appium import webdriver


def init_driver():
    # set up appium
    return webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            "udid": "00008027-001A00901EEB002E",
            "bundleId": "com.brinkventures.blackout",
            "platformName": "iOS",
            "platformVersion": "13.3",
            "deviceName": "Plus’s iPad Pro 11”",
            "xcodeOrgId": "ASYJQU7J4H",
            "xcodeSigningId": "Nick Grout",
        })

@pytest.fixture
def driver():
    driver = init_driver()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
