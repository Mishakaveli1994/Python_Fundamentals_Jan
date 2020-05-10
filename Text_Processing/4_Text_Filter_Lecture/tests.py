import unittest
from solution import solution


class SolutionsTest(unittest.TestCase):
    def test_solution(self):
        banned_words = ["Linux", "Windows"]
        text = "It is not Linux, it is GNU/Linux. Linux is merely the kernel," \
               " while GNU adds the functionality. Therefore" \
               " we owe it to them by calling the OS GNU/Linux! Sincerely," \
               " a Windows client"

        result = solution(banned_words, text)
        expected_result = "It is not *****, it is GNU/*****. ***** is merely the kernel," \
                          " while GNU adds the functionality. Therefore" \
                          " we owe it to them by calling the OS GNU/*****! Sincerely," \
                          " a ******* client"

        self.assertEqual(result, expected_result)
