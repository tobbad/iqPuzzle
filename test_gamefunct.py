#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on 16.2.2014

    Rotate keys

    @author: Tobias Badertscher

"""
import sys
import unittest
from  iqPuzzle import rotateKey
from iqPuzzle import key12 as okey 
import numpy as np
import copy
dir()
class TestRotateKeys(unittest.TestCase):
    def setUp(self):
        print("Start Test")
        pass

    def tearDown(self):
        print("Tear down test")
        pass
    
    def test_Rot(self):
        pass


    def test_Rotate_0(self):
        print("Rotate 0 Degree")
        key=okey()
        expLayout0=okey()
        res = rotateKey(key,0) # is[[1,0,0,0], [1,1,1,1]]
        self.assertTrue(key==res)

    #@unittest.skip("Skip 90 rotation test")
    def test_Rotate_90(self):
        print("Rotate 90 Degree")
        key=okey()
        expKey= okey()#[[1,1,0,0], [0,1,1,1]]
        expKey.figure=np.transpose(np.array([[1,1],[1,0], [1,0],[1,0]]))
        res = rotateKey(key,90)
        self.assertTrue(res==expKey)

    #@unittest.skip("Skip 180 rotation test")
    def test_Rotate_180(self):
        print("Rotate 180 Degree")
        key=okey()
        expKey= okey()
        expKey.figure=np.array([[1,1,1,1],[0,0,0,1] ])
        res = rotateKey(key,180)
        self.assertTrue(res==expKey)

    #@unittest.skip("Skip 270 rotation test")
    def test_Rotate_270(self):
        print("Rotate 270 Degree")
        key=okey()
        expKey= okey()
        expKey.figure=np.array([[0,1],[0,1], [0,1],[1,1]])
        res = rotateKey(key,270)
        self.assertTrue(res==expKey)


if __name__ == '__main__':
    unittest.main()
