# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_dp = [1 for _ in range(n)]
        curr_dp = [1 for _ in range(n)]

        for i in range(1, m):
            for j in range(1, n):
                curr_dp[j] = curr_dp[j - 1] + prev_dp[j]
            curr_dp, prev_dp = prev_dp, curr_dp

        return prev_dp[-1]