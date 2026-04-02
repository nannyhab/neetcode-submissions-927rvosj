class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0

        for R in range(len(prices)):
            
            if prices[R] - prices[L] < 0:
                L = R

            else:
                profit = max(profit, prices[R]-prices[L])

        return profit


