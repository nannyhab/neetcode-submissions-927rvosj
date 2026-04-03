class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        payout = 0

        for R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L = R
            else:
                payout = max(payout, prices[R] - prices[L])
        return payout

