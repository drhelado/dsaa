class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        output = []

        n = len(nums)

        l, r = 0, n - 1

        # traverse array with both pointers
        while l <= r:

            lv = nums[l]**2
            rv = nums[r]**2

            # insert values from biggest to smallest
            # because we know the array in sorted in non-decreasing order
            # meaning in increasing order but can contain duplicates
            if lv > rv:
                output.append(lv)
                l += 1
            else:
                output.append(rv)
                r -= 1

        # return reversed array (smallest to largest)
        return output[::-1]
