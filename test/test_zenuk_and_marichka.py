import unittest
from src.zenuk_and_marichka  import seeding_plan

class TestSeedingPlan(unittest.TestCase):
    def test_5_5(self):
        seeds = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
        expected_plan = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 21, 22, 23, 24, 25]
        self.assertEqual(seeding_plan(5, 5, seeds), expected_plan)
    
    def test_2_4(self):
        seeds = [[1, 2, 3, 4], [5, 6, 7, 8]]
        expected_plan = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(seeding_plan(2, 4, seeds), expected_plan)
    
    def test_1_6(self):
        seeds = [[1, 2, 3, 4, 5, 6]]
        expected_plan = [1, 2, 3, 4, 5, 6]
        self.assertEqual(seeding_plan(1, 6, seeds), expected_plan)
    
    def test_6_1(self):
        seeds = [[1], [2], [3], [4], [5], [6]]
        expected_plan = [1, 2, 3, 4, 5, 6]
        self.assertEqual(seeding_plan(6, 1, seeds), expected_plan)

if __name__ == '__main__':
    unittest.main()
