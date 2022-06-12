class Solution:
    def longestPalindrome(self, s: str) -> str:


        result = ''
        resultLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i # start from the same point and expand both ways, length will be odd
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultLen:
                    result = s[l:r + 1]
                    resultLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1 # start at two different points, length will be even
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultLen:
                    result = s[l:r + 1]
                    resultLen = r - l + 1
                l -= 1
                r += 1

        return result
