class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:

            add = numbers[left] + numbers[right]

            if add == target:
                return [left + 1, right + 1]

            if add > target:
                right -= 1
            elif add < target:
                left += 1
