class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        profitArray = []
        lowest = prices[0]
        size = len(prices)
        for i in range(size):
            if prices[i] < lowest:
                lowest = prices[i]
            profitArray.append(prices[i] - lowest)
        maxProfit = max(profitArray)
        return maxProfit
