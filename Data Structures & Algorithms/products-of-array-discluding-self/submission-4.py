class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [1] * len(nums)
        left, right = 1, 1
        for i in range(1, len(nums)):
            final[i] = nums[i - 1] * left
            left = final[i]
        for i in range(len(nums) - 2, -1, -1):
            final[i] *= (nums[i + 1] * right)
            right = nums[i + 1] * right
        return final
        