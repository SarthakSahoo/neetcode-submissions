import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        f = 1
        for _ in range(abs(n)):
            f *= x
            print(f)
        return f if n > 0 else 1/f