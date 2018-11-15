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
        self.driver.find_element_by_xpath('//*[@data-qa-selector="%s"]' %element).click()

    def choose_a_value_in_a_select(self, select_name, visible_text):
        select = Select(self.driver.find_element_by_name('%s' %select_name))

        options = select.options

        for option in options:
            if option.text == visible_text:
                option_selected = option
                break
            else:
                pass

        select.select_by_visible_text('%s' %visible_text)

        wait = WebDriverWait(self.driver, 8)
        wait.until(EC.element_selection_state_to_be(option_selected, is_selected=True))
