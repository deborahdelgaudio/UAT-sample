from all_imports import *
from user import *

class Test_search_functionality(unittest.TestCase):

    def setUp(self):
        path = os.getcwd() + '/chrome-driver/chromedriver'
        self.driver = webdriver.Chrome(executable_path=path)
        global url
        url = 'https://www.autohero.com/de/search/'

    def test_if_items_are_correctly_filtered_and_sorted(self):
        driver = self.driver

        #verify the url status
        user = User(driver)
        user.check_url_status(url)

        #get url
        driver.get(url)

        #click web element


        #choose 2015 on year select

        #sort by desc price


        ##verify that items are filtered by year
        ##verify that items are sorted by desc price
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()