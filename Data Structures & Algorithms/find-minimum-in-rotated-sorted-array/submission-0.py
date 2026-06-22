class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = nums[0]
        for nums in nums:
            m = min(m, nums)
        return m