class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev, curr = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = max(curr, nums[i] + prev)
            prev, curr = curr, temp
        return curr