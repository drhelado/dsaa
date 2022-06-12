class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        output = []

        n = len(nums)

        for i in range(n):
            # get the index number i points to (-1 because index starts from 0)
            j = abs(nums[i]) - 1

            # if it's a negative value, we have already been here, so it's a duplicate
            # append the number (+1 because j is an index) it to the output array
            if nums[j] < 0:
                output.append(j + 1)

            # set number at current index to negative
            nums[j] = -nums[j]

        return output
