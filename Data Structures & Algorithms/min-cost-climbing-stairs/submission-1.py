class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ways = [0] * len(cost)
        ways[0], ways[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            ways[i] = cost[i] + min(ways[i - 1], ways[i - 2])

        return min(ways[-1], ways[-2])