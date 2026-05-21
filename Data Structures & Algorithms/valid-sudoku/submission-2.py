class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            hashmap = set()
            for i in row:
                if i == ".":
                    continue
                if i in hashmap:
                    return False
                else:
                    hashmap.add(i)
            
        for i in range(len(board)):
            hashmap = set()
            for row in board:
                if row[i] == ".":
                    continue
                if row[i] in hashmap:
                    return False
                else:
                    hashmap.add(row[i])
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                hashmap = set()
                for i in range(3):
                    for j in range(3):
                        val = board[row + i][col + j]
                        if val == ".":
                            continue
                        if val in hashmap:
                            return False
                        hashmap.add(val)
        
        return True
