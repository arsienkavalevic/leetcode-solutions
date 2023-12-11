# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:
            i = self.get_char_index(s, i)
            j = self.get_char_index(t, j)

            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0:
                return False
            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1
        return True

    def get_char_index(self, s, i):
        skips = 0
        while i >= 0:
            if s[i] == "#":
                skips += 1
            elif skips > 0:
                skips -= 1
            else:
                break
            i -= 1
        return i