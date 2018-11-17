import tests.test_search_functionality as test_search_functionality
from tests.all_imports import *
import HtmlTestRunner

# pip install html-testRunner

'''Initialize TestSuite and add TestCase'''
search_functionality_suite = unittest.TestSuite()
search_functionality_suite.addTest(
    unittest.TestLoader().loadTestsFromTestCase(test_search_functionality.Test_search_functionality)
)

'''Run TestSuite'''
runner = HtmlTestRunner.HTMLTestRunner(output='.')
runner.run(search_functionality_suite)