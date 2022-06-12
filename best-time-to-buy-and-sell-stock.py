class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        smallest = max(prices)
        profit = 0

        for i, p in enumerate(prices):

            if p < smallest:
                smallest = p
            elif p - smallest > profit:
                profit = p - smallest

        return profit

        
