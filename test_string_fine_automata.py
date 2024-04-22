import unittest
import sys
sys.path.append('c:/Python/PycharmProjects/programming_part2')
from src.string_finite_automata import search_inText, nextState, automaton_matcher
NO_OF_CHARS = 256

class TestStringMatching(unittest.TestCase):
    def test_nextState(self):
        needle = "AABA"
        m = len(needle)
        self.assertEqual(nextState(needle, m, 0, ord('A')), 1)
        self.assertEqual(nextState(needle, m, 1, ord('A')), 2)
        self.assertEqual(nextState(needle, m, 2, ord('B')), 3)
        self.assertEqual(nextState(needle, m, 3, ord('A')), 4)
        # Test fallback to zero
        self.assertEqual(nextState(needle, m, 3, ord('C')), 0)
        self.assertEqual(nextState(needle, m, 2, ord('A')), 1)

    def test_automaton_matcher(self):
        needle = "ABC"
        TF = automaton_matcher(needle, len(needle))
        self.assertEqual(len(TF), 4)  # Including state 0
        self.assertEqual(TF[0][ord('A')], 1)
        self.assertEqual(TF[1][ord('B')], 2)
        self.assertEqual(TF[2][ord('C')], 3)
        self.assertEqual(TF[3][ord('A')], 0)

    def test_search_inText(self):
        needle = "AABA"
        haystack = "AABAACAADAABAAABAA"
        results = search_inText(needle, haystack, len(needle), len(haystack))
        self.assertEqual(results, [0, 9, 13])
        needle = "AAC"
        results = search_inText(needle, haystack, len(needle), len(haystack))
        self.assertIsNone(results)
        needle = "LONGNEEDLE"
        haystack = "SHORT"
        results = search_inText(needle, haystack, len(needle), len(haystack))
        self.assertIsNone(results)

if __name__ == '__main__':
    unittest.main()



