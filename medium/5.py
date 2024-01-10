# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_len = 1
        result = s[0]

        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]

        right = 1
        center = 1

        for i in range(len(s)):
            if dp[i] < right:
                dp[i] = min(right-i, dp[2*center-i])
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1
            if i+dp[i] > right:
                center = i
                right = i+dp[i]
            if dp[i] > max_len:
                max_len = dp[i]
                result = s[i-dp[i]:i+dp[i]+1].replace('#', '')
        return result