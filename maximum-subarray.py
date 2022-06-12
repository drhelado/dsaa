class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Kadanes algorithm
        max_ending = 0
        max_so_far = max(nums)
        # msf = nums[0]

        for i in nums:
            max_ending += i
            if max_ending < i:
                max_ending = i
            if max_so_far < max_ending:
                max_so_far = max_ending

        return max_so_far
        
