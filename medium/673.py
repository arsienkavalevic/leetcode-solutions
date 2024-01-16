# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)

        lengths, counts = [1 for _ in range(n)], [1 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        max_length = max(lengths)
        return sum(count for length, count in zip(lengths, counts) if length == max_length)