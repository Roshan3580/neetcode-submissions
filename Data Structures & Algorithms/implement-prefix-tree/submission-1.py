class TrieNode:
    def __init__(self):
        self.endofWord = False
        self.children = [None]*26

class PrefixTree:

    def __init__(self):
        self.tree = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.tree
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.endofWord = True

    def search(self, word: str) -> bool:
        curr = self.tree
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return curr.endofWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.tree
        for char in prefix:
            index = ord(char) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return True
        