class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        stack = []
        val = 0
        for token in tokens:
            if is_number(token):
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num2 / num1))
        return stack.pop()