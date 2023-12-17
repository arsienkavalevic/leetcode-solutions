# https://leetcode.com/problems/permutations-ii/

class Solution:
    def backtrack(self, current, nums):
        if current == len(nums):
            self.result.append(nums[:])
            return

        for i in range(current, len(nums)):
            nums[current], nums[i] = nums[i], nums[current]

            self.backtrack(current + 1, nums)

            nums[current], nums[i] = nums[i], nums[current]
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        self.backtrack(0, nums)

        return set(tuple(sequence) for sequence in self.result)