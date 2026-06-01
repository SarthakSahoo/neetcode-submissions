class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        list1 = []
        for i in range(n):
            if nums[i] in list1:
                return True
            if nums[i] not in list1:
                list1.append(nums[i])
                if len(list1) > k:
                    list1.pop(0)
        return False