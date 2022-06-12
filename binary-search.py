class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)

        if n == 0:
            return -1

        l, r = 0, n - 1 # this is the index

        # start moving the pointers
        while l <= r:
            # find the middle index
            # m = l + (r - l) // 2
            m = (l + r) // 2

            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1

        # return -1 if number not found
        return -1
