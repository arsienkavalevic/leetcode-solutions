# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        min_depth = 1

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if not node.left and not node.right:
                    return min_depth

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            min_depth += 1

        return min_depth