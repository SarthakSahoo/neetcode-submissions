class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')': '(', '}': '{', ']': '['}
        x = []
        for char in s:
            if char in dict1:
                if len(x) == 0:
                    return False
                elif x[-1] == dict1[char]:
                    x.pop()
                else:
                    return False
            else:
                x.append(char)
        return True if len(x) == 0 else False