#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on 16.2.2014

    Rotate keys

    @author: Tobias Badertscher

"""
import sys
import unittest
from  iqPuzzle import *

class TestRotateKeys(unittest.TestCase):
    def setUp(self):
        print("Start Test")
        pass

    def tearDown(self):
        print("Tear down test")
        pass
    
    

    def test_Rotate_0(self):
        print("Rotate 0 Degree")
        key={'color':TRED, 'tile':[[1,1,1,1], [1,0,0,0]], 'pos':(7,1), 'text':'F1'} #RED
        expKey=[[1,1,1,1], [1,0,0,0]]
        res = rotateKey(key,0)
        self.assertEqual(res, expKey)


if __name__ == '__main__':
    unittest.main()
