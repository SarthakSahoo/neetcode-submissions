class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_sqr(n: int) -> int:
            output = 0
            while n:
                digit = n % 10
                output += (digit * digit)
                n = n // 10
            return output
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum_of_sqr(n)
            if n == 1:
                return True
        return False
        