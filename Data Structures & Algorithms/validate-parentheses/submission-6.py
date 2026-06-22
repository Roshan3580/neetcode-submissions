class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(':')', '[':']', '{':'}'}
        stack = []

        for c in s:
            if c in pair:
                stack.append(c)
            else:
                if stack and pair[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return not stack