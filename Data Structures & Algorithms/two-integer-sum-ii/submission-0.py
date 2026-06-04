class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, num in enumerate(numbers):
            comp = target - num
            if comp in numbers[0:index]:
                return [numbers.index(comp) + 1, index + 1]