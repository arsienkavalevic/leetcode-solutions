# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = sum(nums[:k])
        nums_sum = result
        for i in range(k, len(nums)):
            nums_sum += nums[i]
            nums_sum -= nums[i - k]
            result = max(result, nums_sum)
        return result / k