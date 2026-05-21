class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False
    def add_word(self, word):
        curr = self
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.endofword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        ROWS, COLUMNS = len(board), len(board[0])
        visited = set()
        result = set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLUMNS or (r,c) in visited or board[r][c] not in node.children):
                return
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endofword == True:
                result.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLUMNS):
                dfs(r, c, root, "")
            
        return list(result)
        