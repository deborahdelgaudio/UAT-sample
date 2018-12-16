from tests.test_search_functionality import TestSearchFunctionality
from tests.all_imports import *

'''Initialize TestSuite and add TestCase'''
search_functionality_suite = unittest.TestSuite()
search_functionality_suite.addTest(
    unittest.defaultTestLoader.loadTestsFromTestCase(TestSearchFunctionality)
)

'''Run TestSuite'''
runner = HtmlTestRunner.HTMLTestRunner(verbosity=2, output='.')
runner.run(search_functionality_suite)
