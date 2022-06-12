class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # nums.sort()
        # print(nums)
        output = []

        # for i in range(0, len(nums)):
        for i in nums:
            index = abs(i) - 1 # take the absolute value here because we could have already modified it to negative, but we are not counting negatives on this loop
            if nums[index] > 0:
                # nums[index] = -nums[index]
                nums[index] *= -1

        for i,v in enumerate(nums):
            if v > 0:
                output.append(i+1)


        return output
