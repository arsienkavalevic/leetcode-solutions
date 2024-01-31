# https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        while left < right:
            pos = left + ((right - left) // 2)
            if x <= arr[pos]:
                right = pos
            elif arr[pos+k] <= x:
                left = pos + 1
            else:
                dist = abs(x - arr[pos])
                k_dist = abs(x - arr[pos+k])
                if dist <= k_dist:
                    right = pos
                else:
                    left = pos + 1
        return arr[left:left+k]