# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def get_max(node):
            if not node:
                return 0
            left = get_max(node.left)
            right = get_max(node.right)
            maximum = node.val + max(left, right)
            return max(maximum, 0)
        result = float('-inf')
        def dfs(node):
            nonlocal result
            if not node:
                return 
            left = get_max(node.left)
            right = get_max(node.right)
            result = max(result, node.val + left + right)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return result