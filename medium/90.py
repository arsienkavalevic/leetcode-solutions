# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            subsets += [subset + [num] for subset in subsets]

        result = set(tuple(sorted(subset)) for subset in subsets)

        return result