class Solution:
    def climbStairs(self, n: int) -> int:

        # base cases
        if n <= 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        n1, n2 = 1, 2
        # while n2 < n:
        for i in range(2, n):
            n1, n2 = n2, n1 + n2

        return n2
