# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        elem_sum = (n + (n * n)) // 2
        return elem_sum - sum(nums)