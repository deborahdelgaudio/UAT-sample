from all_imports.all_imports import *
'''
    User implements user's actions on browser
'''

class User ():

    def __init__(self, driver):
        self.driver = driver

    def check_url_status(self, url):
        res = requests.get(url)
        if res.status_code == 200:
            pass
        else:
            self.fail('Bad status code: %s' % res.status_code)

    def click_a_web_element(self, data_qa_selector):
        self.driver.find_element_by_xpath('//*[@data-qa-selector="%s"]' % data_qa_selector).click()

    def choose_a_value_in_a_select(self, select_name, data_qa_selector):
        select = Select(self.driver.find_element_by_name('%s' % select_name))
        options = select.options

        for option in options:
            if option.get_attribute('data-qa-selector-value') == data_qa_selector:
                corresponding_value = option.get_attribute('value')
                element_selected = option
                break
            else:
                pass

        select.select_by_value('%s' % corresponding_value)

        wait = WebDriverWait(self.driver, 8)
        wait.until(EC.element_to_be_selected(element_selected))