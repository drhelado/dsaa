class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # memo = { i : n for i, n in enumerate(nums) }
        memo = { i : 1 for i in range(len(nums)) } # return max will return max key
        # print(memo)

        n = len(nums)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # print('i, j', (nums[i], nums[j]))
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], memo[j] + 1)

        print(memo)
        return memo[max(memo, key=memo.get)]
