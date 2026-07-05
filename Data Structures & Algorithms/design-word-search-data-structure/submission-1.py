class TrieNode:
    def __init__(self):
        self.endofWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endofWord = True

    def search(self, word: str) -> bool:
        def recur(j, node):
            cur = node
            for i in range(j, len(word)):
                if word[i] == '.':
                    for value in cur.children.values():
                        if recur(i + 1, value):
                            return True
                    return False
                else:
                    if word[i] not in cur.children:
                        return False
                    cur = cur.children[word[i]]
            return cur.endofWord
        return recur(0, self.root)