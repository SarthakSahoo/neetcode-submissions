class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = []
        bucket = [[] for _ in range(len(nums))]
        dict1 = {}
        for num in nums:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1
        
        for key, value in dict1.items():
            bucket[value - 1].append(key)
        print(bucket)
        for i in range(len(bucket) - 1, -1, -1):
            print('Bucket: ', bucket[i])
            if len(bucket[i]) > 0:
                s += bucket[i]
                k -= len(bucket[i])
                if k == 0:
                    break
        return s