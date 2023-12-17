# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self, node, sub_node):
        if not node and not sub_node:
            return True
        if not node or not sub_node or node.val != sub_node.val:
            return False
        return self.compare(node.left, sub_node.left) and self.compare(node.right, sub_node.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])
        
        while queue:
            node = queue.popleft()

            if self.compare(node, subRoot):
                return True

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False