class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(len(nums)):
            j, k = i - 1, i + 1
            ls, rs = 1, 1
            while j > -1:
                ls *= nums[j]
                j -= 1
            
            while k < len(nums):
                rs *= nums[k]
                k += 1
            print(ls, rs)
            final.append(ls * rs)
        return final
        