class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for i, n in enumerate(nums):
            if target - n in map:
                f = map[target - n]
                s = i
                return [f, s]
            else:
                map[n] = i
