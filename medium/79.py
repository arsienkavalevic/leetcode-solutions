# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.traversal(board, i, j, word):
                    return True
        return False

    def traversal(self, board, i, j, word):
        if len(word) == 0:
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False

        value = board[i][j]
        board[i][j] = "#"

        top = self.traversal(board, i - 1, j, word[1:])
        bottom = self.traversal(board, i + 1, j, word[1:])
        left = self.traversal(board, i, j - 1, word[1:])
        right = self.traversal(board, i, j + 1, word[1:])

        board[i][j] = value

        return top or bottom or left or right