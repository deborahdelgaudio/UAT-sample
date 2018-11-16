# -*- coding: utf-8 -*-
from all_imports import *

# user() implements user's actions on browser

class User ():

    def __init__(self, driver):
        self.driver = driver

    def check_url_status(self, url):
        res = requests.get(url)
        if res.status_code == 200:
            pass
        else:
            self.fail(msg='Bad status code: %s' % res.status_code)

    def click_a_web_element(self, element):
        self.driver.find_element_by_xpath('//*[@data-qa-selector="%s"]' % element).click ()

    ('\n'
     '    :params\n'
     '    \n'
     '    select_name type:string     the value of attribute "name" of the select\n'
     '    qa_selector type:string     the value of attribute "data-qa-selector-value" of an option\n'
     '    \n'
     '    :returns\n'
     '    \n'
     '    the option checked \n'
     '    ')
    def choose_a_value_in_a_select(self, select_name, qa_selector):
        select = Select(self.driver.find_element_by_name('%s' % select_name))
        options = select.options

        for option in options:
            if option.get_attribute('data-qa-selector-value') == qa_selector:
                corresponding_value = option.get_attribute('value')
                element_selected = option
                break
            else:
                pass

        select.select_by_value('%s' % corresponding_value)

        wait = WebDriverWait(self.driver, 8)
        wait.until(EC.element_to_be_selected(element_selected))