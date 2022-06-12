class Solution:
    def rob(self, nums: List[int]) -> int:

        # can be done with a boolean checking if first value was used or not maybe

        if len(nums) == 1:
            return nums[0]

        def strike(array):
            two_before = 0
            one_before = 0

            for i, n in enumerate(array):

                # if i == len(nums) - 1:
                    # tmp = max(two_before + n, one_before)
                # else:
                tmp = max(two_before + n, one_before)
                two_before = one_before
                one_before = tmp

            return one_before

        print(nums[1:])
        print(nums[:-1])

        return max(strike(nums[1:]), strike(nums[:-1]))
