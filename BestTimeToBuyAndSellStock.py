class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        curr_profit = 0
        curr_max = 0
        max_profit = 0
        curr_price = prices[-1]
        
        for index in xrange(len(prices) - 1, -1, -1):
            curr_profit = curr_price - prices[index]
            if curr_profit < 0:
                curr_price = prices[index]
            curr_max = max(curr_profit, curr_max)
            max_profit = max(max_profit, curr_max)

        return max_profit