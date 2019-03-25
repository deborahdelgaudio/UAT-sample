# -*- coding: UTF-8 -*-
from test_manager import test_manager
import unittest
import time
import yaml
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

class SearchFunctionalityScenario(unittest.TestCase):

    '''Start web driver'''
    def setUp(self):

        self.d= test_manager.driver.get_driver()

        with open(test_manager.conf_path, "r") as conf:
            self.data = yaml.load(conf, Loader=yaml.FullLoader)
        self.url = self.data["url"]

        self.d.get(self.url)
        time.sleep(1.5)
        self.d.find_element(By.XPATH, "//div[@data-qa-selector='{}']".format(self.data["data_qa_selector"][0])).click()
        time.sleep(1.5)

        year_select = Select(self.d.find_element_by_name('%s' % self.data["selects"][0]))
        year_select.select_by_value("4")

        sort_select = Select(self.d.find_element_by_name('%s'%self.data["selects"][1]))
        sort_select.select_by_value("2")

    '''Stop web driver'''
    def tearDown(self):
        self.d.quit()

    def test_if_items_are_correctly_filtered_and_sorted(self):
        """Test if items are correctly filtered and sorted"""

        current_url = self.d.current_url

        '''Verify that items has been filtered by checking: query string on url, applied filter and registration date on cards'''
        self.assertIn('yearMin=2016', current_url, 'Query string is incorrect {}'.format(current_url))
        time.sleep(2)
        try:
            filter_applied = self.d.find_element_by_xpath('//*[@data-qa-selector="{}"]'.format(self.data["data_qa_selector"][3]))
            value_filter_applied = filter_applied.get_attribute('data-qa-selector-value')
            value_filter_applied = int(value_filter_applied)
            self.assertEqual(value_filter_applied, 2016)
        except:
            self.fail('It\'s not possible to see the active filter \'Registration year\'')

        spec_list = self.d.find_elements_by_xpath('//*[@data-qa-selector=""]'.format(self.data["data_qa_selector"][4]))

        reg_dates = []
        for spec in spec_list:
            date = spec.find_elements_by_xpath('//*[@data-qa-selector=""]'.format(self.data["data_qa_selector"][5]))[0]
            reg_dates.append(date)

        reg_years = []
        for date in reg_dates:
            date_str = str(date.text.encode('ascii', 'replace')).split('/')[1]
            year = int(date_str)
            reg_years.append(year)

        self.assertTrue((all(year >= 2016 for year in reg_years)), "Registration years are not correctly selected")


        '''Verify that items are sorted by descending price by checking: query string and price on cards'''
        self.assertIn('sort=PRICE_DESC', current_url, 'Query string is incorrect {}'.format(current_url))

        prices = self.d.find_elements_by_xpath('//*[@data-qa-selector=""]'.format(self.data["data_qa_selector"][6]))

        price_list = []
        for price in prices:
            p = str(price.text.encode('ascii','replace')).split(' ')[0].replace('.', '')
            p = int(p)
            price_list.append(p)

        self.assertTrue(all(first >= second for first, second in zip(price_list, price_list[1:])))

if __name__ == "__main__":
    unittest.main()