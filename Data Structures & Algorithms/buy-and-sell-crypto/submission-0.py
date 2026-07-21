class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r = 0,1 #l buy, r  is sell
        maxP = 0 #initialize tot rack profit

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l =r
            r+=1
        return maxP
        
        #two pointers
        #l,r o,1 apart, l = buy, r sell
        #check profit if left value < right value store the maaxP
        #else need to move pointer l= r , r+=1