import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_short_vardecl(self):
        """Test short variable declaration"""
        input = """foo: function void (inherit a: integer, inherit out b: float) inherit bar {}
            main: function void () {
            printInteger(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
