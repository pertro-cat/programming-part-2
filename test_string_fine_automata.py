import unittest
import sys
sys.path.append('c:/Python/PycharmProjects/programming_part2')

from src.string_finite_automata import transition_table, finite_automaton

class TestStringFiniteAutomata(unittest.TestCase):

    def test_empty_needle(self):
        nedle = ""
        haystack = "AABAACAADAABAAABAA"
        transition_table_result = transition_table(nedle)
        result = finite_automaton(haystack, nedle, transition_table_result)
        self.assertEqual(result, -1)

    def test_empty_haystack(self):
        nedle = "AABA"
        haystack = ""
        transition_table_result = transition_table(nedle)
        result = finite_automaton(haystack, nedle, transition_table_result)
        self.assertEqual(result, -1)

    def test_needle_larger_than_haystack(self):
        nedle = "LONGNEEDLE"
        haystack = "SHORT"
        transition_table_result = transition_table(nedle)
        result = finite_automaton(haystack, nedle, transition_table_result)
        self.assertEqual(result, -1)

    def test_all_parameters_correct(self):
        nedle = "AABA"
        haystack = "AABAACAADAABAAABAA"
        transition_table_result = transition_table(nedle)
        result = finite_automaton(haystack, nedle, transition_table_result)
        self.assertEqual(result, [0, 9, 13])

if __name__ == '__main__':
    unittest.main()


