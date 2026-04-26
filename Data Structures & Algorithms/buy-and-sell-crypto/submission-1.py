class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1

        while r < len(prices):
            print(profit)
            if prices[l] > prices[r] and r + 1 != len(prices):
                l = r
                r += 1
            profit = max(profit, prices[r] - prices[l])
            r += 1

        return profit
            
        