class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashmap = {}

        for i, n in enumerate(nums):
            if n in hashmap:
                return True

            hashmap[n] = i

        return False
