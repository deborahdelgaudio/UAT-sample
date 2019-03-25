# coding=utf-8
from driver import Driver

class TestManager():
    """
    class that helps to manage test cases
    :@return object
    """

    def __init__(self):

        self.scenario = None
        self.browser = None
        self.viewport = None
        self.driver = None
        self.conf_path = None

    def SetUp(self, scenario, browser, viewport, conf_path):

        self.scenario = scenario
        self.browser = browser
        self.viewport = viewport
        self.driver = Driver(browser, viewport)
        self.conf_path = conf_path


test_manager = TestManager()