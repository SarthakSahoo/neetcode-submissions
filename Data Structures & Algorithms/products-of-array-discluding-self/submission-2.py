class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1] * len(nums), [1] * len(nums)
        prefix[0], suffix[-1] = 1, 1
        prefix[1], suffix[-2] = nums[0], nums[-1]
        final = []
        for i in range(2, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        print(prefix)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        print(suffix)
        for i in range(len(nums)):
            final.append(prefix[i] * suffix[i])
        return final
        