import unittest
from solution import reverse


class SolutionTests(unittest.TestCase):
    def test_if_that_reverse_function_actually_reverses(self):
        self.assertEqual(reverse('asd'), 'dsa')
        self.assertEqual(reverse('baba'), 'abab')

    def test_word_that_is_symetric_returns_the_same(self):
        self.assertEqual(reverse('bob'), 'bob')
        self.assertEqual(reverse('drop'), 'pord')
