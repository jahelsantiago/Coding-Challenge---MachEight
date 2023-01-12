import unittest

def pair_sums(nums, target):
    """
    Return list of all pairs of integers in nums that sum to target.
    """
    nums = sorted(nums)
    pairs = []
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            pairs.append((nums[left], nums[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return pairs