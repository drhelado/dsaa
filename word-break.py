class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)

        memo = [False] * (n + 1)
        memo[-1] = True

        # print(memo)

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                _w = len(w)
                if (i + _w) <= n and s[i: i + _w] == w:
                    print('i, i+w', (i, i+_w))
                    memo[i] = memo[i + _w]

                if memo[i]:
                    break

        print(memo)

        return memo[0]






        '''#  T O(n * m) S O(n)

        # one dimensional array cache
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # out of bounds is true

        # bottom up
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # check if there are enough characters in string to compare

                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break

        return dp[0]'''
                    
