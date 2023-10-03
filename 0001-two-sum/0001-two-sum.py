class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i,x in enumerate(nums):
            value = target - x
            if value in hashset:
                return [hashset[value],i]
            hashset[x] = i
        return 