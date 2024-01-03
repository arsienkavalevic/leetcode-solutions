# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        hash_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        result = []

        def backtrack(current, digits_left):
            if len(digits_left) == 0:
                result.append(current)
                return
            for letter in hash_map[digits_left[0]]:
                backtrack(current + letter, digits_left[1:])
            return

        backtrack("", digits)
        return result