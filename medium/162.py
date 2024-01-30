# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            pos = left + ((right - left) // 2)
            if nums[pos] < nums[pos + 1]:
                left = pos + 1
            else:
                right = pos
        return left