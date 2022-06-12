class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Boyer Moore Algorithm
        output = 0

        count = 0

        for n in nums:

            # set output to n
            if count == 0:
                output = n

            # increment 1 if n = output, else decrement 1
            if n == output:
                count += 1
            else:
                count -= 1

        return output
