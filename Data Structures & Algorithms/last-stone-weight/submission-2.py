import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-val for val in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            first = -1 * heapq.heappop(max_heap)
            second = -1 * heapq.heappop(max_heap)
            diff = abs(first - second)
            diff = -1 * diff if diff < 0 else diff
            if diff > 0:
                heapq.heappush(max_heap, -1 * diff)
        return 0 if not len(max_heap) else -max_heap[0]

