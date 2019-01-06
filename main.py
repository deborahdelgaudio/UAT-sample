import argparse
import glob
import importlib
import inspect
import sys,os
folders = ['tests', 'utility']
sys.path.insert(0, os.getcwd()+'/config/')

for folder in folders:
    sys.path.insert(0, os.getcwd() + '/src/' + folder)

from test_manager import test_manager
from test_config import url
import unittest
import HtmlTestRunner

def get_parameters():
    parser = argparse.ArgumentParser (description='** Search functionality tester **')

    parser.add_argument ('-u', '--url', help='specify url', type=str, default=url)
    parser.add_argument ('-s', '--scenario', help='specify the name of the scenario', type=str, default='search_functionality')
    parser.add_argument('-d', '--driver', help='specify where is the diver binary, if doesn\'t execute it on docker set the path of your local webdriver file', default= '/usr/local/bin/chromedriver')
    parser.add_argument ('-b', '--browser', help='specify browser', type=str, default='chrome', choices=['chrome', 'firefox -->not available on container!'])
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

if __name__ == "__main__":

    test_manager.SetUp(get_parameters().url,get_parameters().scenario,get_parameters().browser,get_parameters().viewport, get_parameters().driver)

    '''Initialize TestSuite and add TestCase'''
    suite = unittest.TestSuite()

    for testclass in get_test_case_class():
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(testclass))

    if get_parameters().html_report == 'y':
        '''Run TestSuite with HtmlTestRuner'''
        runner = HtmlTestRunner.HTMLTestRunner(verbosity=2, output='.')
        runner.run(suite)
    else:
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)