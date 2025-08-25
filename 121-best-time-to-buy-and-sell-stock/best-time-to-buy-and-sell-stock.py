class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        

        l = 0
        maxProfit = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)

        return maxProfit
