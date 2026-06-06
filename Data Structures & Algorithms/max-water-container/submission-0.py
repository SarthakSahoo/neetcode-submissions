class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        n = len(heights)
        for i in range(n):
            for j in range(i + 1, n):
                temp = min(heights[i], heights[j]) * (j - i)
                m = max(m, temp)
        return m