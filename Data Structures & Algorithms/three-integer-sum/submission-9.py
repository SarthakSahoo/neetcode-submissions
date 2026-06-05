class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        seen = {}
        s = set()
        for i in range(n):
            rem = 0 - nums[i]
            for j in range(i + 1, n):
                comp = rem - nums[j]
                if comp in seen:
                    if i != j and j != seen[comp] and i != seen[comp]:
                        triplet = tuple(sorted([nums[i], nums[j], comp]))
                        if triplet not in s:
                            s.add(triplet)
                seen[nums[j]] = j
        return [list(val) for val in s]