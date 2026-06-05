class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [0] * (n + 1)
        # dp[0], dp[1] = 1, 1
        prev, new = 1, 1
        for i in range(2, n + 1):
            temp = prev + new
            prev, new = new, temp
        return new