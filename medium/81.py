# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            pos = left + ((right - left) // 2)
            if nums[pos] == target:
                return True
            if nums[left] == nums[pos]:
                left += 1
                continue
            if nums[left] < nums[pos]:
                if nums[left] <= target <= nums[pos]:
                    right = pos - 1
                else:
                    left = pos + 1
            else:
                if nums[pos] <= target <= nums[right]:
                    left = pos + 1
                else:
                    right = pos - 1
        return False