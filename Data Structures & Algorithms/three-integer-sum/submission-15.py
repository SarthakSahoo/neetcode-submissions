class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        
        s = []
        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                temp = nums[l] + nums[r] + nums[i]
                if temp == 0:
                    triplet = [nums[i], nums[l], nums[r]]
                    if triplet not in s:
                        s.append(triplet)
                    l += 1
                    r -= 1
                elif temp > 0:
                    r -= 1
                else:
                    l += 1
        return s