# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter, length, matched = Counter(s1), len(s1), 0
        for i in range(len(s2)):
            if s2[i] in counter:
                counter[s2[i]] -= 1
                if counter[s2[i]] == 0:
                    matched += 1
            if i >= length and s2[i-length] in counter:
                if counter[s2[i-length]] == 0:
                    matched -= 1
                counter[s2[i-length]] += 1
            if matched == len(counter):
                return True
        return False