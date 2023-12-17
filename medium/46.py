# https://leetcode.com/problems/permutations/description/

class Solution:
    def backtrack(self, current, nums):
        if current == len(nums):
            self.result.append(nums[:])
            return

        for i in range(current, len(nums)):
            nums[current], nums[i] = nums[i], nums[current]

            self.backtrack(current + 1, nums)

            nums[i], nums[current] = nums[current], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        self.backtrack(0, nums)

        return self.result