# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traversal(node):
            if not node:
                return [None]
            return [node.val] + traversal(node.left) + traversal(node.right)
        print(traversal(p), traversal(q))
        return traversal(p) == traversal(q) 
