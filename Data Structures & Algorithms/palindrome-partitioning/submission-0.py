class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []
        def dfs(i, j):
            if j == len(s):
                res.append(partition.copy())
                return

            if i >= len(s):
                return
                
            if isValid(s, j, i):
                partition.append(s[j:i+1])
                dfs(i + 1, i + 1)
                partition.pop()
            
            dfs(i+1, j)
                
        def isValid(s, j, i):
            l, r = j, i
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        dfs(0, 0)
        return res