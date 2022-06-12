class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        rows = text1
        cols = text2

        rows = len(text1)
        cols = len(text2)

        memo = [[0 for j in range(rows + 1)] for i in range(cols + 1)]

        # print(memo)

        for i in range(cols -1, -1, -1):
            for j in range(rows - 1, -1, -1):

                # if text1[i] == text2[j]:
                if text2[i] == text1[j]:
                    # get previous (one forward since we're going backwards) and add 1 since the letters match
                    previous_bottom_right = memo[i + 1][j + 1]
                    memo[i][j] = previous_bottom_right + 1
                else:
                    right = memo[i][j + 1]
                    bottom = memo[i + 1][j]
                    memo[i][j] = max(right, bottom)

        return memo[0][0]
