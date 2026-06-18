class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index_popped = stack.pop()
                l[index_popped] = i - index_popped
            stack.append(i)
        return l