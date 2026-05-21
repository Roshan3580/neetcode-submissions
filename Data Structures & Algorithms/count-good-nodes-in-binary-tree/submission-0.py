# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(node, maximum):
            nonlocal result
            if not node:
                return None
            if node.val >= maximum:
                result += 1
            dfs(node.left, max(maximum, node.val))
            dfs(node.right, max(maximum, node.val))           

        dfs(root, root.val)
        return result