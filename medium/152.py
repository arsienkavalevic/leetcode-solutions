# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max, current_min = 1, 1
        result = nums[0]

        for num in nums:
            values = (num, num * current_max, num * current_min)
            current_max, current_min = max(values), min(values)

            result = max(result, current_max)
        
        return result