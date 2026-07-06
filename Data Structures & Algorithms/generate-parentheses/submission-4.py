class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, ope, clo):
            if len(curr) == 2*n:
                res.append(curr)
                return
            if ope < n:
                dfs(curr + '(', ope+1, clo)
            if clo < ope:
                dfs(curr + ')', ope, clo+1)
        
        dfs("", 0, 0)
        return res