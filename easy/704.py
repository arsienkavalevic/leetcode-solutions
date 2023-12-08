# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pos = left + ((right - left) // 2)
            if nums[pos] == target:
                return pos
            if nums[pos] < target:
                left = pos + 1
            elif nums[pos] > target:
                right = pos - 1
        return -1