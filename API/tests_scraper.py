# -*- coding: utf-8 -*-
from pydoc import html
from unittest import TestCase
import unittest
from Scraped import *


class TestScrapper(TestCase):
    def setUp(self): 
        self.scrapper = Scraped()
        self.urlConnectStr ="https://pythonprogramming.net/parsememcparseface/"
        self.scrapper.read_dict()
        self.scrapper.iterate_table()

    def test_dict(self):
        expected = {'Program Name': {0: 'Python', 1: 'Pascal', 2: 'Lisp', 3: 'D#', 4: 'Cobol', 5: 'Fortran', 6: 'Haskell'}, 'Internet Points': {0: 932914021, 1: 532, 2: 1522, 3: 12, 4: 3, 5: 52124, 6: 24}, 'Kittens?': {0: 'Definitely', 1: 'Unlikely', 2: 'Uncertain', 3: 'Possibly', 4: 'No.', 5: 'Yes.', 6: 'lol.'}}
        self.assertEqual(self.scrapper.read_dict(), expected)

if __name__ == "__main__":
    unittest.main()