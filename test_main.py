from numpy import array
import numpy as np
import unittest
from main import strassen, calcula_m, calcula_c


class MainTest(unittest.TestCase):

    def test_3x3(self):
        A = array([[1, 2, 3], [2, 3, 4], [2, 3, 4]])
        B = array([[11, 12, 13], [31, 52, 53], [51, 22, 13]])
        expected = A.dot(B)
        estimated = strassen(A, B)
        self.assertTrue(np.all(expected == estimated))

    def test_2x2(self):
        A = array([[1, 2], [3, 4]])
        B = array([[2, 3], [3, 5]])
        expected = A.dot(B)
        estimated = strassen(A, B)
        self.assertTrue(np.all(expected == estimated))

    def test_4x4(self):
        A = array([[10, 20, 30, 40], [11, 22, 33, 44], [21, 22, 23, 24], [51, 72, 83, 94]])
        B = array([[11, 12, 13, 14], [17, 22, 32, 24], [31, 52, 53, 54], [51, 22, 13, 14]])
        expected = A.dot(B)
        estimated = strassen(A, B)
        self.assertTrue(np.all(expected == estimated))

    def test_8x8(self):
        A = array([[1, 2, 3, 4, 11, 12, 13, 14], [11, 12, 13, 14, 1, 2, 3, 4], [11, 12, 13, 14, 1, 2, 3, 4],
                   [11, 12, 13, 14, 1, 2, 3, 4], [1, 2, 3, 4, 11, 12, 13, 14], [1, 2, 3, 4, 11, 12, 13, 14],
                   [11, 12, 13, 14, 1, 2, 3, 4], [1, 2, 3, 4, 11, 12, 13, 14]])
        B = array([[11, 12, 13, 14, 11, 12, 13, 14], [12, 22, 32, 24, 11, 12, 13, 14], [31, 52, 11, 12, 13, 14, 53, 54],
                   [51, 11, 12, 13, 14, 22, 13, 14], [1, 2, 3, 4, 11, 12, 13, 14], [1, 2, 3, 4, 11, 12, 13, 14], [11, 12, 13, 14, 1, 2, 3, 4],
                   [11, 12, 13, 14, 1, 2, 3, 4]])
        expected = A.dot(B)
        estimated = strassen(A, B)
        self.assertTrue(np.all(expected == estimated))


    def test_calcula_m(self):
        m1,m2,m3,m4,m5,m6,m7 = calcula_m(1,1,2,2,3,3,4,4)
        self.assertEquals(m1, 21)
        self.assertEquals(m2, 12)
        self.assertEquals(m3, -1)
        self.assertEquals(m4, 2)
        self.assertEquals(m5, 8)
        self.assertEquals(m6, 6)
        self.assertEquals(m7, -8)

    def test_calcula_c(self):
        c11,c12,c21,c22 = calcula_c(1,2,3,4,5,6,7)
        self.assertEquals(c11, 7)
        self.assertEquals(c12, 8)
        self.assertEquals(c21, 6)
        self.assertEquals(c22, 8)

