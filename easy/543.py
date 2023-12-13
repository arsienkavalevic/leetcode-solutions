# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter

    def dfs(self, node):
        if not node:
            return -1
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.diameter = max(self.diameter, left + right + 2)
        return 1 + max(left, right)