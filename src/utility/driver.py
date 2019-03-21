# coding=utf-8
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver import Remote, ChromeOptions, FirefoxOptions
import socket

class Driver():

    def __init__(self, browser, viewport):
        self.browser = browser
        self.viewport = viewport
        self.driver = self.set_driver()


    def build_driver_parameters(self):

        global options, profile, capabilities

        if 'chrome' in self.browser:
            profile = None
            options = ChromeOptions()
            options.add_argument ('--no-sandbox')
            options.add_argument ('--headless')
            options.add_argument ('--disable-gpu')
            capabilities = DesiredCapabilities.CHROME

        else:

            options = FirefoxOptions()
            profile = FirefoxProfile()
            capabilities = DesiredCapabilities.FIREFOX

        if 'mobile' in self.viewport:
            options.add_argument ('--window-size=320,768')
        elif 'desktop' in self.viewport:
            options.add_argument('--window-size=1366,768')

        return options, profile, capabilities

    def set_driver(self):

        hostname = socket.gethostname()
        executor = "http://{localhost}:4444/wd/hub".format(localhost=hostname)
        opt , prf , cap = self.build_driver_parameters()
        self.driver = Remote(command_executor=executor, desired_capabilities=cap, browser_profile=prf, options=opt)

    def get_driver(self):

        return self.driver