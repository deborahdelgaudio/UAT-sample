# coding=utf-8
from all_imports import *
from get_driver import GetDriver

class TestManager():
    """
    class that helps to manage test cases
    :@return object
    """

    def __init__(self):
        self.url = None
        self.scenario = None
        self.browser = None
        self.viewport = None
        self.driver = None

    def SetUp(self, url, scenario, browser, viewport, driver_path):

        self.url = url
        self.scenario = scenario
        self.browser = browser
        self.viewport = viewport

        self.driver = GetDriver(browser, viewport, driver_path)


test_manager = TestManager()