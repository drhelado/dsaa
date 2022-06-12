class Solution:
    def reverseBits(self, n: int) -> int:

        # T O(1) S O(1)

        result = 0

        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31 - i))

        return result
