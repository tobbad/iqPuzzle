#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on 16.2.2014

    Test for fixpoint

    @author: Tobias Badertscher

"""
import sys
import unittest
from  iqPuzzle import *

class test_rotate(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRot0(self):
        key={'color':TRED, 'tile':[[1,1,1,1], [1,0,0,0]], 'pos':(7,1), 'text':'F1'} #RED
        expKey=[[1,1,1,1], [1,0,0,0]]
        res = rotateKey(key,0)
        self.assertEqual(res, expKey)


if __name__ == '__main__':
    unittest.main()
