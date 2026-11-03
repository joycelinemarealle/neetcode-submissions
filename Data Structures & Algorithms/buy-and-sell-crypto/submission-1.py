class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #buy low sell high
        #l buy #sell as day
        #if prices[r] > price[l] i am going to make profit
        #if not move l=r, 
        #then move r to next day
        #return maxP
        l,r = 0,1 #buy and sell
        maxP = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l=r
            r+=1
        return maxP
