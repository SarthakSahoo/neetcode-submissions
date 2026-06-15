class Solution:
    def countBits(self, n: int) -> List[int]:
        s = []
        for i in range(n + 1):
            s.append(bin(i).count('1'))
        return s