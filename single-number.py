class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0

        # using bit manipulation - XOR all elemnts, if it doesn't have a match, that element will be returned
        for i in range(len(nums)):
            result ^= nums[i]

        return result
