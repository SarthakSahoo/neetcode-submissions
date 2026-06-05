class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        
        s = []
        for i in range(n - 2):
            l, r = i + 1, n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while l < r:
                temp = nums[l] + nums[r] + nums[i]
                if temp == 0:
                    triplet = [nums[i], nums[l], nums[r]]
                    s.append(triplet)
                    l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif temp > 0:
                    r -= 1
                else:
                    l += 1
        return s