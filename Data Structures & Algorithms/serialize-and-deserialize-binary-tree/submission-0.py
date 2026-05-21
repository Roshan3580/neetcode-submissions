# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        array = []
        def dfs(node):
            if node == None:
                array.append("null")
                return
            array.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(",".join(array))
        return ",".join(array)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        array = data.split(',')
        i = 0
        def dfs():
            nonlocal i
            if array[i] == "null":
                i += 1
                return None
            node = TreeNode(int(array[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

