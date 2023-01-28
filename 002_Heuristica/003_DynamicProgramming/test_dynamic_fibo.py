import unittest

from dynamic_fibonacci import dynamic_fibonacci


class MyTest(unittest.TestCase):
    def test_example_checks(self):
        self.assertEqual(1, dynamic_fibonacci(1))
        self.assertEqual(1, dynamic_fibonacci(2))

    def test_other_checks(self):
        self.assertEqual(2, dynamic_fibonacci(3))
        self.assertEqual(3, dynamic_fibonacci(4))
        self.assertEqual(5, dynamic_fibonacci(5))
        self.assertEqual(8, dynamic_fibonacci(6))

    def test_slow_tests(self):
        self.assertEqual(9227465, dynamic_fibonacci(35))

    def test_stack_overflow_tests(self):
        self.assertEqual(9227465, dynamic_fibonacci(3529))
