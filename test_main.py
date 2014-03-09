from numpy import array
import unittest
from main import strassen


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
