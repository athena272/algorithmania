import unittest

from slow_fibonacci import slow_fibonacci


class MyTest(unittest.TestCase):
    def test_example_checks(self):
        self.assertEqual(1, slow_fibonacci(1))
        self.assertEqual(1, slow_fibonacci(2))

    def test_other_checks(self):
        self.assertEqual(2, slow_fibonacci(3))
        self.assertEqual(3, slow_fibonacci(4))
        self.assertEqual(5, slow_fibonacci(5))
        self.assertEqual(8, slow_fibonacci(6))

    def test_slow_tests(self):
        self.assertEqual(9227465, slow_fibonacci(35))
