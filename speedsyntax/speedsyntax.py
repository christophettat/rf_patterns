from robot.api import SuiteVisitor
import re

"""
This prerunmodifier will reduce syntax check by removing any occurence of a keywork already seen at least once
THis assumes that tests are built around the same keywords and that syntax checking one occurence is enough
"""

class speedsyntax(SuiteVisitor):

    def __init__(self):
        self.KW_seen = []

    def start_test(self,test):
        stripped = lambda k : re.sub('[\'"].*?[\'"]','',k) #remove any embedded parameter between quotes 
        test.body=[k for k in test.body if stripped(k.name) not in self.KW_seen] # only keep new keywords
        self.KW_seen.extend([stripped(k.name) for k in test.body]) # add any new keyword to the list of kw to skip


    def end_suite(self, suite):
        """drop any test that is empty + drop empty suites"""
        suite.tests = [t for t in suite.tests if len(t.body)>0] #remove empty tests
        suite.suites = [s for s in suite.suites if s.test_count > 0] # remove empty suites


