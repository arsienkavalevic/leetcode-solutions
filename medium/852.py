# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            pos = left + ((right - left) // 2)
            if arr[pos] < arr[pos + 1]:
                left = pos + 1
            else:
                right = pos
        return left