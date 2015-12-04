import unittest

from compare_versions import core

class TestSemVer(unittest.TestCase):

    def testSpec2(self):
        self.assertTrue(core.verify_list(['1.9.0','1.10.0','1.11.0'], 'lt'))
        self.assertFalse(core.is_valid('01.1.1'))
        self.assertFalse(core.is_valid('-1.1.1'))
        self.assertFalse(core.is_valid('1.1'))
        self.assertFalse(core.is_valid('1.1.1.1'))

    def testSpec9(self):
        self.assertTrue(core.is_valid('1.0.0-alpha'))
        self.assertTrue(core.is_valid('1.0.0-alpha.1'))
        self.assertTrue(core.is_valid('1.0.0-0.3.7'))
        self.assertTrue(core.is_valid('1.0.0-x.7.z.92'))

    def testSpec10(self):
        self.assertTrue(core.is_valid('1.0.0-alpha+001'))
        self.assertTrue(core.is_valid('1.0.0+20130313144700'))
        self.assertTrue(core.is_valid('1.0.0-beta+exp.sha.5114f85'))
        self.assertTrue(core.verify_list(['1.0.0','1.0.0+1','1.0.0+2'], 'eq'))

    def testSpec11(self):
        self.assertTrue(core.verify_list(['1.0.0','2.0.0','2.1.0','2.1.1'], 'lt'))
        self.assertTrue(core.verify_list(['1.0.0-alpha','1.0.0-alpha.1','1.0.0-alpha.beta','1.0.0-beta','1.0.0-beta.2','1.0.0-beta.11','1.0.0-rc.1','1.0.0'], 'lt'))

