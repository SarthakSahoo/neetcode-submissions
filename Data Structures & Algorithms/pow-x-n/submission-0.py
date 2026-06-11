import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        y = abs(n)
        f = 1
        for _ in range(y):
            f *= x
            print(f)

        if n > 0:
            return f
        else:
            return 1/f