#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
class Test(unittest.TestCase):
    def testMi(self):
        result = 9-0
        hope = 9
        self.assertEqual(result,hope)
    def testPlus(self):
        result = 9/3
        hope = 2
        self.assertNotEqual(result,hope)
if __name__ == '__main__':
    unittest.main()