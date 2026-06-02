class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        val = 0
        min_val = prices[0]
        for i in range(0, len(prices)):
            min_val = min(prices[i], min_val)
            val = max(val, prices[i] - min_val)
        return val