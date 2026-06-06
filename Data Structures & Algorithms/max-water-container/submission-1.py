class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_cost = 0
        m, n = 0, len(heights) - 1
        while m < n:
            temp_cost = min(heights[m], heights[n]) * (n - m)
            max_cost = max(max_cost, temp_cost)

            if heights[m] < heights[n]:
                m += 1
            else:
                n -= 1
        return max_cost