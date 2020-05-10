import unittest
from solution import repeat_by_length
from solution import repeat_each_word_by_length


class SolutionTest(unittest.TestCase):
    def test_repeat_works(self):
        result = repeat_by_length("add")
        expected_result = "addaddadd"
        self.assertEqual(result, expected_result)

    def test_repeat_list_of_words_by_their_lenght(self):
        result = repeat_each_word_by_length(['hi', 'abc', 'add'])
        expected_result = 'hihiabcabcabcaddaddadd'
        self.assertEqual(result, expected_result)

    def test_performance(self):
        repeat_each_word_by_length(["asd", "asd"] * 100000)
