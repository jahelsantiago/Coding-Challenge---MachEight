from pair_sums import pair_sums
import unittest 

class TestPairSums(unittest.TestCase):
    def test_correct_pairs(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 8
        expected = [(1, 7), (2, 6), (3, 5)]
        self.assertEqual(pair_sums(nums, target), expected)

    def test_no_matching_pairs(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 19
        expected = []
        self.assertEqual(pair_sums(nums, target), expected)

    def test_empty_input(self):
        nums = []
        target = 10
        expected = []
        self.assertEqual(pair_sums(nums, target), expected)
    
    def test_target_zero(self):
        nums = [-1, -2, -3, -4, 4, 3, 2, 1, 9]
        target = 0
        expected = [(-4,4), (-3,3), (-2,2), (-1,1)]
        self.assertEqual(pair_sums(nums, target), expected)
        
    def test_target_negative(self):
        nums = [-10, 2, -6, -2, -5, -3, 7, 8, 9]
        target = -8
        expected = [(-10,2), (-6,-2), (-5,-3)]
        self.assertEqual(pair_sums(nums, target), expected)
        

if __name__ == '__main__':
    unittest.main()