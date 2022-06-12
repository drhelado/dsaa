class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        # second solution (checking only 1s)
        result = 0

        while n:
            n = n & (n - 1)
            result += 1

        return result
        '''


        # first solution (checking all digits)

        # T O(1) S O(1)
        result = 0

        while n:
            result += n % 2
            n = n >> 1

        return result
