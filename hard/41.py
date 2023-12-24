# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            val = abs(nums[i])
            if val > n:
                continue
            val -= 1
            if nums[val] > 0:
                nums[val] *= -1

        for i in range(n):
            if nums[i] >= 0:
                return i + 1
            
        return n + 1