class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        val = 0
        for i in range(0, len(prices)):
            min_val = min(prices[0:i + 1])
            val = max(val, prices[i] - min_val)
        return val