class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)

        memo = {} # (index, sum)

        def backtrack(i, s):

            if i == n:
                if s == target:
                    return 1
                else:
                    return 0

            if (i, s) in memo:
                return memo[(i, s)]

            p = backtrack(i + 1, s + nums[i])
            m = backtrack(i + 1, s - nums[i])

            # print('p', (p))

            memo[(i, s)] = (p + m)

            # print(memo[(i, s)])

            return memo[(i, s)]

        return backtrack(0, 0)
