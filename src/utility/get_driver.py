# coding=utf-8
from all_imports import *
from selenium import webdriver

class GetDriver():

    def __init__(self, browser, viewport, driver_path):
        self.browser = browser
        self.viewport = viewport
        self.driver = None
        self.driver_path = driver_path

    def __add_options(self):

        if 'chrome' in self.browser:
            options = webdriver.ChromeOptions()
            options.add_argument ('--no-sandbox')
            options.add_argument ('--headless')
            options.add_argument ('--disable-gpu')
            if 'mobile' in self.viewport:
                options.add_argument ('--window-size=320,768')
            elif 'desktop' in self.viewport:
                options.add_argument('--window-size=1366,768')
            else:
                print('There was a problem with viewport parameter set: {}'.format(self.viewport))
                sys.exit()
        #else: TO DO With firefox


        return options

    def build_driver(self):

        options = self.__add_options()
        if 'chrome' in self.browser:
            self.driver = webdriver.Chrome(options=options, executable_path=self.driver_path)
        #else: TO DO with firefox

        return self.driver