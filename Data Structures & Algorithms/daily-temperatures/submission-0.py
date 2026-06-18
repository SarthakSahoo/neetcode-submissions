class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    l[i] = j - i
                    break
        return l