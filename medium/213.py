# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(nums, n):
            dp = [0 for i in range(n)]
            dp[0] = nums[0]
            dp[1] = max(nums[1], dp[0])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        return max(robber(nums[1:], n - 1), robber(nums[:-1], n - 1))