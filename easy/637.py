# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])

        result = []

        while queue:
            n = len(queue)
            layer_sum = 0
            for _ in range(n):
                node = queue.popleft()
                layer_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(layer_sum / n)
        return result