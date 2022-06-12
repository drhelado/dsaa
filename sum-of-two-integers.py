class Solution:
    def getSum(self, a: int, b: int) -> int:


        while b:
            _a = (a & b) << 1
            a = a ^ b
            b = _a
            # return a

        return a
