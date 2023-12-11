# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0
        while len(nums_set) > 0:
            num = nums_set.pop()
            next_num = num + 1
            while next_num in nums_set:
                nums_set.remove(next_num)
                next_num += 1
            prev_num = num - 1
            while prev_num in nums_set:
                nums_set.remove(prev_num)
                prev_num -= 1
            longest_sequence = max(longest_sequence, next_num - prev_num - 1)
        return longest_sequence