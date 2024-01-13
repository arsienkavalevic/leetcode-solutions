# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        current, one_back, two_back = 0, 1, 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                current = 0
            else:
                current = one_back
                if i + 1 < len(s) and s[i] + s[i + 1] <= '26':
                    current += two_back
            two_back, one_back = one_back, current
            
        return current