class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        

        l = 0
        r = l + 1
        maxProfit = 0

        if len(prices) < 2:
            return 0

        if len(prices) < 3:
            profit = prices[r] - prices[l]
            if profit > 0: return profit

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
                r += 1

        return maxProfit
