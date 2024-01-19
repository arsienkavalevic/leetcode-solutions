# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)

        if nums_sum % k > 0:
            return False

        target_sum = nums_sum // k
        dp = [0 for _ in range(k)]
        nums.sort(reverse=True)

        def backtrack(i):
            if i == len(nums):
                return True

            for j in range(k):
                if dp[j] + nums[i] <= target_sum:
                    dp[j] += nums[i]

                    if backtrack(i + 1):
                        return True
                        
                    dp[j] -= nums[i]

                    if dp[j] == 0:
                        break
            return False
        
        return backtrack(0)