class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        hash = {}
        totalPairs = 0

        for num in time:
            modNum = num % 60

            if modNum == 0:
                if 0 in hash:
                    totalPairs += hash[0]
            elif (60 - modNum) in hash:
                totalPairs += hash[60 - modNum]

            if modNum in hash:
                hash[modNum] += 1
            else:
                hash[modNum] = 1

        return totalPairs
