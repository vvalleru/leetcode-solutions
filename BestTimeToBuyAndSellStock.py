class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        max_profit = 0
        curr_profit = 0
        curr_sell_price = 0

        for day in xrange(len(prices) - 1, -1 , -1):
            curr_sell_price = max(curr_sell_price, prices[day])
            curr_profit = max(curr_profit, curr_sell_price - prices[day])
            max_profit = max(max_profit, curr_profit)

        return max_profit