# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
            
        result = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                for suffix in self.partition(s[i:]):
                    result.append([s[:i]] + suffix)
        return result