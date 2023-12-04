#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        return len(nums) > len(num_set)