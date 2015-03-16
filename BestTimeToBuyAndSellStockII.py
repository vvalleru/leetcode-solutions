class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        N = len(prices)
        possibleProfits = [0]
        if N < 2:
            return 0

        start = 0
        result = 0

        while start < N:
            while start + 1 < N and prices[start + 1] < prices[start]:
                start += 1

            end = start

            while end + 1 < N and prices[end + 1] > prices[end]:
                end += 1

            possibleProfits.append(prices[end] - prices[start])
            start = end + 1

        if len(possibleProfits) > 2:
            possibleProfits.sort()
            result = possibleProfits[-1] + possibleProfits[-2]
        else:
            result = sum(possibleProfits)

        return result