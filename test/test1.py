import unittest
import classifierlib
import utils
import numpy as np

class Test1(unittest.TestCase):
    def test_flatten(self):
        test_arr=np.array([[1,2,3], [4,5,6]])
        res_arr=utils.flatten_ndim(test_arr)
        self.assertEqual(True, res_arr.all() == np.array([1.,2.,3.,4.,5.,6.]).all())

if __name__ == '__main__':
	unittest.main()
