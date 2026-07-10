class Solution:
    def checkValidString(self, s: str) -> bool:
        op = []
        star = []
        for idx, char in enumerate(s):
            if char == "(":
                op.append(idx)
            elif char == "*":
                star.append(idx)
            else:
                if not op and not star:
                    return False
                if op:
                    op.pop()
                else:
                    star.pop()

        while op and star:
            if op.pop() > star.pop():
                return False

        return not op