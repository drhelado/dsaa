class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        _set = set()
        left = 0
        result = 0

        for c in range(len(s)):
            while s[c] in _set:
                _set.remove(s[left])
                left += 1

            _set.add(s[c])

            result = max(result, c - left + 1) # adding one because c and left are indexes, starting from 0

        return result
