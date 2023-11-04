class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i,j in enumerate(nums):
            result = target-j
            if result in dictionary : return [dictionary[result], i]
            dictionary[j] = i