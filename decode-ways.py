class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)

        memo = { n : 1 } # bottom up

        print(memo)

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                memo[i] = 0
            else:
                memo[i] = memo[i + 1]

            if (i + 1 < len(s)):
                if (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                    memo[i] += memo[i + 2]

            print(memo)

        return memo[0]



        '''memo = { len(s) : 1 }

        def dfs(i):
            print(memo)

            if i in memo:
                return memo[i]

            if s[i] == '0':
                return 0

            result = dfs(i + 1)

            if (i + 1 < len(s)):
                if (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                    result += dfs(i + 2)

            memo[i] = result

            return result

        print(memo)

        return dfs(0)'''
