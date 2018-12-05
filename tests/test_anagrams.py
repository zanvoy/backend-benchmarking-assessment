""" Test Suite for anagrams module. """
import unittest
from timeit import Timer
from anagrams import find_anagrams


class TestAnagrams(unittest.TestCase):
    """
        Benchmarking test case. We test actual functionality of find_anagrams
        with doctests, which is why this test case excludes those unit tests.
    """

    def setUp(self):
        with open("words/short.txt") as f:
            self.short = f.read().split()

        with open("words/long.txt") as f:
            self.long = f.read().split()

    def test_short(self):
        """ Test find_anagrams with short word list. """
        benchmark = 0.005  # seconds
        my_time = Timer(lambda: find_anagrams(self.short)).timeit(number=1)
        my_time = round(my_time, 3)
        failure_text = (
            'find_anagrams took {} seconds, which exceeds the '
            'benchmark of {} seconds'.format(my_time, benchmark)
            )
        self.assertTrue(my_time <= benchmark, failure_text)

    @unittest.skip("Remove this line once short test passes")
    def test_long(self):
        """ Test find_anagrams with long word list. """
        benchmark = 0.010  # seconds
        my_time = Timer(lambda: find_anagrams(self.long)).timeit(number=1)
        my_time = round(my_time, 3)
        failure_text = (
            'find_anagrams took {} seconds, which exceeds the '
            'benchmark of {} seconds'.format(my_time, benchmark)
            )
        self.assertTrue(my_time <= benchmark, failure_text)
