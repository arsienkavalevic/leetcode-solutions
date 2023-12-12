# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.result = []
        self.traversal("", s, 0)
        return self.result

    def traversal(self, current, s, i):
        if len(current) == len(s):
            self.result.append(current)
            return

        self.traversal(current + s[i], s, i + 1)
        if s[i].isalpha():
            self.traversal(current + s[i].swapcase(), s, i + 1)
        return