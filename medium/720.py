# https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words)

        word_set, result = set(), ""

        word_set.add("")

        for word in words:
            if word[:-1] in word_set:
                if len(word) > len(result):
                    result = word
                word_set.add(word)

        return result