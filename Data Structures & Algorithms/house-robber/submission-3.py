class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, len(nums)):
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3] if (i - 3) >= 0 else 0)
            print(dp)
        return max(dp[-1], dp[-2])