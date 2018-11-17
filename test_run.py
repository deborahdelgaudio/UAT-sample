import tests.test_search_func
import unittest
# import HTMLTestRunner pip install html-testRunner

'''Initialize TestSuite and add TestCase'''
search_functionality_suite = unittest.TestSuite()
search_functionality_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.test_search_func.Test_search_functionality))

'''Run TestSuite'''
unittest.TextTestRunner(verbosity=2).run(search_functionality_suite)