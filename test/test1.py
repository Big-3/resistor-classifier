import unittest
import classifierlib

class Test1(unittest.TestCase):
	
	def test_failing(self):
		self.assertEqual(False, classifierlib.hello() == 'helloworld')

	def test_test(self):
		self.assertEqual(2, 1+1)


if __name__ == '__main__':
	unittest.main()