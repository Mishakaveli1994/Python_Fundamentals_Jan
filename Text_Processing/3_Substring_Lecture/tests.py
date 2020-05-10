import unittest
from solution import solution


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        result = solution('ice', 'kicegiciceeb')
        expected_result = 'kgb'
        self.assertEqual(result, expected_result)
