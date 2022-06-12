class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        if (len(merged) % 2 == 0):
            mid = len(merged) / 2
            return (merged[int(mid - 1)] + merged[int(mid)]) / 2;
        else:
            return merged[int((len(merged) - 1) / 2)]
