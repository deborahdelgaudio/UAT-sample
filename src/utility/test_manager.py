# coding=utf-8
from driver import Driver

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

    def SetUp(self, url, scenario, browser, viewport):

        self.url = url
        self.scenario = scenario
        self.browser = browser
        self.viewport = viewport

        self.driver = Driver(browser, viewport)


test_manager = TestManager()