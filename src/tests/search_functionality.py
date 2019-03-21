# -*- coding: UTF-8 -*-
from test_manager import test_manager
from user import User
from config.test_config import data_qa_selector
from config.test_config import select_name
import unittest
import time

class SearchFunctionalityScenario(unittest.TestCase):

    '''Start web driver'''
    def setUp(self):
        self.driver = test_manager.driver.get_driver()
        self.url = test_manager.url

    '''Stop web driver'''
    def tearDown(self):
        self.driver.quit()

    def test_if_items_are_correctly_filtered_and_sorted(self):
        """Test if items are correctly filtered and sorted"""
        d = self.driver
        user = User(d)

        user.check_url_status(self.url)

        d.get(self.url)

        user.click_a_web_element(data_qa_selector[0])

        user.choose_a_value_in_a_select(select_name[0], data_qa_selector[1])  # choose 2016 on year select

        user.choose_a_value_in_a_select(select_name[1], data_qa_selector[2])  # sort by desc price using a select

        current_url = d.current_url

        '''Verify that items has been filtered by checking: query string on url, applied filter and registration date on cards'''
        self.assertIn('yearMin=2016', current_url, 'Query string is incorrect {}'.format(current_url))
        time.sleep(2)
        try:
            filter_applied = d.find_element_by_xpath('//*[@data-qa-selector="{}"]'.format(data_qa_selector[3]))
            value_filter_applied = filter_applied.get_attribute('data-qa-selector-value')
            value_filter_applied = int(value_filter_applied)
            self.assertEqual(value_filter_applied, 2016)
        except:
            self.fail('It\'s not possible to see the active filter \'Registration year\'')

        spec_list = d.find_elements_by_xpath('//*[@data-qa-selector=""]'.format(data_qa_selector[4]))

        reg_dates = []
        for spec in spec_list:
            date = spec.find_elements_by_xpath('//*[@data-qa-selector=""]'.format(data_qa_selector[5]))[0]
            reg_dates.append(date)

        reg_years = []
        for date in reg_dates:
            date_str = str(date.text.encode('ascii', 'replace')).split('/')[1]
            year = int(date_str)
            reg_years.append(year)

        self.assertGreaterEqual(reg_years, 2016)


        '''Verify that items are sorted by descending price by checking: query string and price on cards'''
        self.assertIn('sort=PRICE_DESC', current_url, 'Query string is incorrect {}'.format(current_url))

        prices = d.find_elements_by_xpath('//*[@data-qa-selector=""]'.format(data_qa_selector[6]))

        price_list = []
        for price in prices:
            p = str(price.text.encode('ascii','replace')).split(' ')[0].replace('.', '')
            p = int(p)
            price_list.append(p)

        self.assertTrue(all(first >= second for first, second in zip(price_list, price_list[1:])))

if __name__ == "__main__":
    unittest.main()