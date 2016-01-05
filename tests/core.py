import unittest

from compare_versions import core


class TestIsValid(unittest.TestCase):

    def testValid(self):
        self.assertTrue(core.is_valid('1.0.0'))
        self.assertTrue(core.is_valid('1.0.0', scheme='string'))
        self.assertTrue(core.is_valid('abcd', scheme='string'))

    def testInvalid(self):
        self.assertFalse(core.is_valid('1.0.0.0'))
        self.assertFalse(core.is_valid('1 0 0'))


class TestVerifyList(unittest.TestCase):

    def testShortList(self):
        self.assertRaises(ValueError, core.verify_list, [])
        self.assertRaises(ValueError, core.verify_list, ['1.0.0'])

    def testInvalidComparison(self):
        self.assertRaises(ValueError, core.verify_list, ['1.0.0', '1.1.0'], comparison='not-a-comparison')

    def testInvalidScheme(self):
        self.assertRaises(ValueError, core.verify_list, ['1.0.0', '1.1.0'], scheme='not-a-scheme')

    def testComparisonsGood(self):
        self.assertTrue(core.verify_list(['1.0.0', '1.0.0'], comparison='eq'))
        self.assertTrue(core.verify_list(['1.0.0', '1.1.0'], comparison='ne'))
        self.assertTrue(core.verify_list(['1.0.0', '1.1.0'], comparison='lt'))
        self.assertTrue(core.verify_list(['1.1.0', '1.0.0'], comparison='gt'))
        self.assertTrue(core.verify_list(['1.0.0', '1.0.0', '1.1.0'], comparison='le'))
        self.assertTrue(core.verify_list(['1.1.0', '1.0.0', '1.0.0'], comparison='ge'))

    def testComparisonsBad(self):
        self.assertFalse(core.verify_list(['1.0.0', '1.1.0'], comparison='eq'))
        self.assertFalse(core.verify_list(['1.0.0', '1.0.0'], comparison='ne'))
        self.assertFalse(core.verify_list(['1.1.0', '1.0.0'], comparison='lt'))
        self.assertFalse(core.verify_list(['1.0.0', '1.1.0'], comparison='gt'))
        self.assertFalse(core.verify_list(['1.1.0', '1.0.0', '1.0.0'], comparison='le'))
        self.assertFalse(core.verify_list(['1.0.0', '1.0.0', '1.1.0'], comparison='ge'))


class TestComparisonSymbol(unittest.TestCase):

    def testSymbols(self):
        self.assertEqual(core.comparison_symbol(1, 1), '==')
        self.assertEqual(core.comparison_symbol(1, 2), '<')
        self.assertEqual(core.comparison_symbol(2, 1), '>')

    def testInvalid(self):
        self.assertRaises(TypeError, core.comparison_symbol, 1, 'two')
