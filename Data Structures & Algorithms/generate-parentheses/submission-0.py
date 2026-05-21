class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(s:str):
            if n*2 == len(s):
                if valid(s):
                    res.append(s)
                return

            dfs(s + '(')
            dfs(s + ')')

        def valid(s:str):
            open = 0
            for c in s:
                if c == '(':
                    open += 1
                else:
                    open -= 1
                if open < 0:
                    return False
            return not open

        dfs("")
        return res
