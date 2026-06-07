class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_sqr(n: int) -> int:
            output = 0
            while n:
                digit = n % 10
                output += (digit * digit)
                n = n // 10
            return output
        slow, fast = n, sum_of_sqr(n)
        while slow != fast:
            slow, fast = sum_of_sqr(slow), sum_of_sqr(sum_of_sqr(fast))
        return False if fast != 1 else True
        