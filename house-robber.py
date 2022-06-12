class Solution:
    def rob(self, nums: List[int]) -> int:

        two_before = 0
        one_before = 0

        for n in nums:
            # use the biggest value, either n - 2 + n or n - 1
            tmp = max(two_before + n, one_before)
            # shift forward
            two_before = one_before
            one_before = tmp

        # biggest value will be the last one, two
        return one_before
