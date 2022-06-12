class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # T O(n * n) S O(1)

        # use gauss's formula for T O(1)

        result = len(nums)

        # this is doing sum of array from 0-n minus sum(nums), but on the fly
        for i in range(len(nums)):
            print('i, nums_i, i - nums_i', (i, nums[i], i - nums[i]))
            result += (i - nums[i])

        return result
