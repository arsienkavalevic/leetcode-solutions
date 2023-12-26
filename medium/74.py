# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(array, target):
            left, right = 0, len(array)

            while left <= right:
                pos = left + ((right - left) // 2)
                if array[pos] == target:
                    return True
                if array[pos] < target:
                    left = pos + 1
                else:
                    right = pos - 1
            return False
        
        left, right = 0, len(matrix) - 1

        while left <= right:
            pos = left + ((right - left) // 2)
            if matrix[pos][0] <= target and matrix[pos][-1] >= target:
                return binarySearch(matrix[pos], target)
            if matrix[pos][0] < target:
                left = pos + 1
            else:
                right = pos - 1
        return False