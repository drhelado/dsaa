class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in coins:
            # print("i", (i))
            for j in range(i, amount + 1):
                # print("j", (j))
                # if j >= i:
                    # print('before', (dp))
                    dp[j] += dp[j - i]
                    # print('after', (dp))


        return dp[amount]
