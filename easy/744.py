# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n - 1
        while left <= right:
            pos = left + (right - left) // 2
            if letters[pos] <= target:
                left = pos + 1
            else:
                right = pos - 1

        if left < n:
            return letters[left]
        return letters[0]