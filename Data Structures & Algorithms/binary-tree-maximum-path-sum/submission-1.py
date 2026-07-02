# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def getMax(node):
            if not node:
                return 0
            left = getMax(node.left)
            right = getMax(node.right)
            path = node.val + max(left, right)
            return max(0, path)

        def dfs(node):
            nonlocal res
            if not node:
                return
            left = getMax(node.left)
            right = getMax(node.right)
            total = node.val+left+right
            res = max(total, res)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res