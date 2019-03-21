import argparse
import glob
import importlib
import inspect
import sys,os
import unittest
import datetime

sys.path.insert(0, os.getcwd()+'/config/')
folders = ['tests', 'utility']
for folder in folders:
    sys.path.insert(0, os.getcwd() + '/src/' + folder)

from test_manager import test_manager
from HTMLTestRunner import HTMLTestRunner

def get_parameters():
    parser = argparse.ArgumentParser (description='** THIS IS A SAMPLE OF User Acceptance Test -- Author: Deborah Del Gaudio **')

    parser.add_argument ('-b', '--browser', help='specify browser', type=str, default='chrome', choices=['chrome', 'firefox -->not available on container!'])
    parser.add_argument('-t', '--testfile', help="specify the testfile that you want to execute", type=str, default='*')
    parser.add_argument ('-v', '--viewport', help='specify on which viewport you want run test', type=str, choices=['mobile', 'desktop'], default='desktop')
    parser.add_argument ('-html', '--html_report', help='set \'n\' to disable html report', type=str, choices=['y', 'n'], default='y')
    output = parser.parse_args ()

    return output

def get_test_case_class():
    modules = glob.glob('src/tests/' + test_manager.scenario + '.py')
    for m in modules:
        file_name,file_ext = os.path.splitext(os.path.basename(m))
        current_module = importlib.import_module(file_name)
        for name, obj in inspect.getmembers(sys.modules[current_module.__name__]):
            if inspect.isclass(obj) and 'Scenario' in obj.__name__:
                yield obj

def run_suite(testSuite):
    if get_parameters().html_report == 'n':
        unittest.TextTestRunner(verbosity=2).run(testSuite)

    else:
        now = str(datetime.datetime.now())

        file_name = "search_functionality_" + get_parameters().browser + '_' + get_parameters().viewport + '_' + now
        suite_title = 'UAT sample'
        description = "Verify the search functionality into a listing page"

        with open('reports/' + file_name + '.html', 'wb') as report:

            runner = HTMLTestRunner(
                stream=report,
                title=suite_title,
                description=description
            )

            runner.run(testSuite)

    return True

if __name__ == "__main__":

    test_manager.SetUp(url="url", scenario=get_parameters().testfile, browser=get_parameters().browser, viewport=get_parameters().viewport)

    '''Initialize TestSuite and add TestCase'''
    suite = unittest.TestSuite()

    for testclass in get_test_case_class():
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(testclass))

    run_suite(suite)