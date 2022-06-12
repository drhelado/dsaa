class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # if len(nums) == 1:
        #     if nums[0] != target:
        #         return -1
        #     else:
        #         return 0

        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = (right + left) // 2
            print('middle, nums', (middle, nums[left:right]))

            if target == nums[middle]:
                return middle

            # left sorted portion
            if nums[middle] >= nums[left]:

                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1

            # right sorted side
            elif nums[middle] < nums[left]:

                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1

        return -1
