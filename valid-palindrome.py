class Solution:
    def isPalindrome(self, s: str) -> bool:

        # two pointers, no extra memory
        left, right = 0, len(s) - 1

        def _isalnum(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))

        while left < right:
            while left < right and not _isalnum(s[left]):
                left += 1
            while right > left and not _isalnum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1

        return True
