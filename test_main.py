from numpy import array
import unittest
from main import strassen, calcula_m, calcula_c


class MainTest(unittest.TestCase):

    def test_1x1(self):
        A = array([1])
        B = array([-1])
        self.assertTrue((array(strassen(A, B)) == A.dot(B)).all())

    def test_2x2(self):
        A = array([[1, 2], [3, 4]])
        B = array([[2, 3], [3, 5]])
        self.assertTrue((array(strassen(A, B)) == A.dot(B)).all())

    def test_4x4(self):
        A = array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
        B = array([[11, 12, 13, 14], [12, 22, 32, 24], [31, 52, 53, 54], [51, 22, 13, 14]])
        self.assertTrue((array(strassen(A, B)) == A.dot(B)).all())


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

