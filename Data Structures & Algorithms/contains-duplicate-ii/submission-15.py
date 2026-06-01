class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        list1 = set()
        for i in range(n):
            if i > k:
                list1.remove(nums[i - k - 1])
            if nums[i] in list1:
                return True
            list1.add(nums[i])
        return False