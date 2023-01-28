import unittest

from better_fibo import better_fibonacci


class MyTest(unittest.TestCase):
    def test_example_checks(self):
        self.assertEqual(1, better_fibonacci(1))
        self.assertEqual(1, better_fibonacci(2))

    def test_other_checks(self):
        self.assertEqual(2, better_fibonacci(3))
        self.assertEqual(3, better_fibonacci(4))
        self.assertEqual(5, better_fibonacci(5))
        self.assertEqual(8, better_fibonacci(6))

    def test_slow_tests(self):
        self.assertEqual(9227465, better_fibonacci(35))

    def test_stack_overflow_tests(self):
        self.assertEqual(9227465, better_fibonacci(3529))
