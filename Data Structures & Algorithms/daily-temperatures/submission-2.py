class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        def top(stack):
            return stack[-1] if len(stack) else -1
        l = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if not len(stack):
                stack.append(i)
            while top(stack) != -1 and temperatures[top(stack)] < temperatures[i]:
                index_popped = stack.pop()
                l[index_popped] = i - index_popped
            stack.append(i)
        return l