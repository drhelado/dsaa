class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # if len(nums) == 1:
            # return nums[0]

        total = max(nums)

        maxCurrent, minCurrent = 1, 1

        for n in nums:

            # if n == 0:
            #     maxCurrent, minCurrent = 1, 1
            #     continue

            _minCurrent = minCurrent * n
            _maxCurrent = maxCurrent * n

            minCurrent = min(_minCurrent, _maxCurrent, n)
            maxCurrent = max(_minCurrent, _maxCurrent, n)

            total = max(minCurrent, maxCurrent, total)

        return total
