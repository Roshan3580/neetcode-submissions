class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        length = n*2
        def dfs(curr, ope, clo):
            if ope < clo or len(curr) > length:
                return
            if len(curr) == length and ope == clo:
                res.append(curr)
                return
            curr += '('
            dfs(curr, ope+1, clo)
            curr = curr[:-1]
            curr += ')'
            dfs(curr, ope, clo+1)
        
        dfs("", 0, 0)
        return res