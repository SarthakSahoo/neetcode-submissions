class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = []
        dict1 = {}
        for num in nums:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1
        dict1 = dict(sorted(dict1.items(), key = lambda item: item[1], reverse=True))
        print(dict1)
        for key, value in dict1.items():
            s.append(key)
            k -= 1
            if k == 0:
                break
        return s