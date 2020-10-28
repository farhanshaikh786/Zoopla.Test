import unittest
import HTMLTestRunner
from unittest import TestLoader
from TestCasesFile import *
import os,time, datetime
class Test(unittest.TestCase):
    def testName(self):
        loader=TestLoader()
        suite=unittest.TestSuite()
        #load=loader.loadTestsFromModule("TestCasesFile.py")
        load=loader.loadTestsFromName("TestCasesFile")
        suite.addTests(load)
        dir=os.getcwd()
        dt=datetime.datetime.now().strftime("%Y_%d_%m_%H%M")
        outputfile=open(dir + "//AutomationTestReport_"+dt+".html","w")
        runner=HTMLTestRunner.HTMLTestRunner(stream=outputfile,title ="Test Execution report", description = "Automation Test")
        runner.run(suite)
        outputfile.close()
if __name__=="__main__":
    unittest.main()