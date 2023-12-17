# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = [(root, "")]
        result = []
        answer = ""
        while stack:
            node, answer = stack.pop()
            answer += str(node.val)

            if not node.left and not node.right:
                result.append(answer)

            if node.left:
                stack.append((node.left, answer + "->"))
            if node.right:
                stack.append((node.right, answer + "->"))
        return result