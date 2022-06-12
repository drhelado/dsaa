class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        output = []

        for i, n in enumerate(nums):
            # print(n)

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                add = nums[i] + nums[left] + nums[right]

                if add == 0:
                    _ = [nums[i], nums[left], nums[right]]
                    # if _ not in output:
                    output.append(_)

                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                    continue

                if add > 0:
                    right -= 1
                elif add < 0:
                    left += 1

        return output
