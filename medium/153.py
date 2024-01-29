# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            pos = left + ((right - left) // 2)
            if nums[pos] > nums[right]:
                left = pos + 1
            else:
                right = pos

        return nums[left]