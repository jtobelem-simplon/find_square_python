#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import find_square



class TestFindSquareMethods(unittest.TestCase):
      
    def setUp(self):
        self.carte = [
            ".....XXXXXXX...............",
            "....oXXXXXXX...............",
            ".....XXXXXXXo..............",
            ".....XXXXXXX...............",
            "....oXXXXXXX...............",
            ".....XXXXXXX...o...........",
            ".....XXXXXXX...............",
            "......o..............o.....",
            "..o.......o................",
        ]
  
    def test_is_free(self):
        self.assertTrue(find_square.is_free(self.carte, 0,5, 3, 'o'), "should find full square")
        self.assertFalse(find_square.is_free(self.carte, 0,5, 9, 'o'), "should not find full square")

    def test_is_valid(self):
        carte_not_ok_1 = [
            "...o",
            "....",
            "...o...",
        ]
        self.assertFalse(find_square.is_map_valid(carte_not_ok_1, 3), "incorrect line size")

        carte_not_ok_2 = [
            "oo"
            "oo"
        ]
        self.assertFalse(find_square.is_map_valid(carte_not_ok_2, 2), "all full lines")

        carte_not_ok_3 = [
            "...o....",
            "...o",
        ]
        self.assertFalse(find_square.is_map_valid(carte_not_ok_3, 3), "incorrect line number")

        carte_not_ok_4 = [
            "...o"
            "..R.",
            "...o",
        ]
        self.assertFalse(find_square.is_map_valid(carte_not_ok_4, 3), "incorrect symbol")

        self.assertTrue(find_square.is_map_valid(self.carte, 9), "should be valid")

  
if __name__ == '__main__':
    unittest.main()