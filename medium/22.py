# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        stack = [(0, 0, "")]

        while stack:
            left, right, s = stack.pop()
            if len(s) == n * 2:
                result.append(s)
            else:
                if left < n:
                    stack.append((left + 1, right, s + "("))
                if right < left:
                    stack.append((left, right + 1, s + ")"))

        return result