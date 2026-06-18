class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        def top(stack):
            return stack[-1] if len(stack) else -1
        l = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if not len(stack):
                stack.append(i)
            print('Stack: ', stack)
            while top(stack) != -1 and temperatures[top(stack)] < temperatures[i]:
                print('Pop: ', stack)
                # if top(stack) == -1:
                #     break
                index_popped = stack.pop()
                l[index_popped] = i - index_popped
                print('L: ', l)
            stack.append(i)
        return l