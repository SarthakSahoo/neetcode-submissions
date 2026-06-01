class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dict1 = dict()
        for i in range(n):
            if nums[i] not in dict1.keys():
                dict1[nums[i]] = i
            else:
                if abs(i - dict1[nums[i]]) <= k:
                    return True
                dict1.pop(list(dict1.keys())[0])
                dict1[nums[i]] = i
        return False