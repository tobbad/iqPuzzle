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
import copy

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
        key=key00()
        expLayout=key00()
        res = rotateKey(key,0)
        self.assertTrue(key==res)

    def test_Rotate_90(self):
        print("Rotate 90 Degree")
        key=key00()
        expKey= key00()
        expKey.figure=np.array([[1,1],[0,1], [0,1],[0,1]])
        res = rotateKey(key,90)
        self.assertTrue(res==expKey)

    def test_Rotate_180(self):
        print("Rotate 180 Degree")
        key=key00()
        expKey= key00()
        expKey.figure=np.array([[0,0,0,1],[1,1,1,1] ])
        res = rotateKey(key,180)
        self.assertTrue(res==expKey)

    def test_Rotate_270(self):
        print("Rotate 270 Degree")
        key=key00()
        expKey= key00()
        expKey.figure=np.array([[1,0],[1,0], [1,0],[1,1]])
        res = rotateKey(key,270)
        self.assertTrue(res==expKey)


if __name__ == '__main__':
    unittest.main()
