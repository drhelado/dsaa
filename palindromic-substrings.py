class Solution:
    def countSubstrings(self, s: str) -> int:


        result = 0

        def countPalindrome(s, l, r):
            result = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
            return result

        for i in range(len(s)):
            result += countPalindrome(s, i, i)
            result += countPalindrome(s, i, i + 1)

        return result
