# https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_sum = sum(nums)

        if nums_sum < abs(target) or (nums_sum + target) % 2 != 0:
            return 0

        def knapsack(target):
            dp = [1] + [0] * nums_sum

            for num in nums:
                for j in range(nums_sum, num - 1, -1):
                    dp[j] += dp[j - num]
            return dp[target]

        return knapsack((nums_sum + target) // 2)