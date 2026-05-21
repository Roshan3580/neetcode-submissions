# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p and q and p.val != q.val:
                return False
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if not root:
            return False
        if not subRoot:
            return True

        if isSameTree(root, subRoot) == True:
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)