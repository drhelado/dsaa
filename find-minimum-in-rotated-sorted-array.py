class Solution:
    def findMin(self, nums: List[int]) -> int:

        '''def bs(array):
            # print(array)

            if len(array) > 1:

                middle = (len(array) // 2) - 1
                # print('middle', (middle))

                if array[middle] == array[-1]:
                    # print('equal', (array[middle]))
                    return middle

                if array[middle] > array[-1]:
                    return bs(array[middle + 1:])
                elif array[middle] < array[-1]:
                    return bs(array[:middle + 1])

                # elif array[middle] == array[-1]

            else:
                # return array[0]
                # print('single value', (array))
                return array[0]

        return bs(nums)'''


        if len(nums) > 1:
            # return nums[0]

            middle = (len(nums) // 2) - 1
            print('nums, middle', (nums, middle))

            if nums[middle] > nums[-1]:
                return self.findMin(nums[middle + 1:])
            elif nums[middle] < nums[-1]:
                return self.findMin(nums[:middle + 1])
            elif nums[middle] == nums[-1]:
            # else:
                # print('return', (nums[:-1]))
                # return self.findMin([nums[middle]])
                return [middle]
                # return self.findMin([nums[0]])

                # return nums[-1]
        else:
            return nums[0]
            # return nums
