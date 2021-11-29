import unittest
import classifierlib

class Test0(unittest.TestCase):
	def test_hello(self):
		self.assertEqual('hello world', classifierlib.hello())


if __name__ == '__main__':
	unittest.main()