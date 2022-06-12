class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        default = amount + 1

        # memo = [default] * default
        # memo[0] = 0

        memo = { 0: 0 }
        for i in range(1, default):
            memo[i] = default

#         print(memo)

        for n in range(1, default):
            # print(n)

            for c in coins:
                if n - c >= 0:
                    difference = n - c
                    # print('n, c, difference', (n, c, difference))
                    memo[n] = min(memo[n], memo[difference] + 1)

        # print(memo)

        if memo[amount] != default:
            return memo[amount]
        else:
            return -1
