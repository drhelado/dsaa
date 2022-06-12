class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        n = len(arr)

        l, r = 0, n - 1

        while l <= r:
            m = l + (r - l) // 2

            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m - 1

        return l
