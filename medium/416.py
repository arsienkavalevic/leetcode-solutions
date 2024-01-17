# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)

        if nums_sum % 2 == 1:
            return False

        target_sum = nums_sum // 2
        dp = [True] + [False for _ in range(target_sum)]

        for num in nums:
            for j in range(target_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[-1]