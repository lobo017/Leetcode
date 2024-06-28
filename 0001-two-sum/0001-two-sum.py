class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i,x in enumerate(nums):
            diff = target - x
            if diff in sums:
                return [sums[diff],i]
            else:
                sums[x] = i
        return
        