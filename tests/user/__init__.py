from all_imports import *
# user implements user's actions on browser


class User():

    def __init__(self, driver):
        self.driver = driver

    def check_url_status(self, url):
        res = requests.get(url)
        if res.status_code == 200:
            pass
        else:
            self.fail(msg='Bad status code: %s' %res.status_code)

    def click_a_web_element(self, element):

        pass

    def choose_a_value_in_a_select(self, select, value):
        pass
