class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        nums = sorted(nums, reverse=True)
        return nums[k-1]
