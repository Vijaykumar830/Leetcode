class Solution(object):
    def maxProfit(self, prices):
        best_buy = prices[0]
        max_profit = 0 

        for i in range(1,len(prices)):
            if prices[i]>best_buy:
                max_profit = max(max_profit,prices[i]-best_buy)
            best_buy = min(best_buy,prices[i])
        return max_profit