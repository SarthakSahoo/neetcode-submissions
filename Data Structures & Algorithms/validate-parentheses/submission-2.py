class Solution:
    def isValid(self, s: str) -> bool:
        
        x = []
        for char in s:
            if char == '(':
                x.append(')')
            elif char == '[':
                x.append(']')
            elif char == '{':
                x.append('}')
            else:
                if len(x) == 0 or x.pop() != char:
                    return False
        return len(x) == 0