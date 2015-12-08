import unittest

from compare_versions import core

class TestString(unittest.TestCase):

    def testAlpha(self):
        self.assertTrue(core.verify_list(['a','b','c'], scheme='string'))

    def testNumeric(self):
        self.assertTrue(core.verify_list(['1','2','3'], scheme='string'))

    def testStandard(self):
        self.assertTrue(core.verify_list(['1.0.0','1.0.1','2.0.0'], scheme='string'))

