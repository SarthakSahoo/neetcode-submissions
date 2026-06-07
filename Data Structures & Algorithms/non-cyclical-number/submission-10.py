class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_sqr(n: int) -> int:
            output = 0
            while n:
                digit = n % 10
                output += (digit * digit)
                n = n // 10
            return output
        while n != 1 and n != 4:
            n = sum_of_sqr(n)
        return n == 1
        