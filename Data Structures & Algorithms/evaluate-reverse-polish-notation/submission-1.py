class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n not in ("+", "-", "*", "/"):
                print(n)
                stack.append(n)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if n == '+':
                    stack.append(a + b)
                elif n == '-':
                    stack.append(a - b)
                elif n == '*':
                    stack.append(a * b)
                elif n == '/':
                    stack.append(a/b)
                else:
                    pass
        return int(stack[0])