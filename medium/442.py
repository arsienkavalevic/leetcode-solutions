# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for i in nums:
            if nums[abs(i) - 1] < 0:
                duplicates.append(abs(i))
            else:
                nums[abs(i) - 1] *= -1
        return duplicates