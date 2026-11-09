class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxP = 0
        l = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxP = max(maxP, prices[r] - prices[l])

        return maxP