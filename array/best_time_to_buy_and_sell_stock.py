class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #O(n) single pass
        
        if prices == []:
            return 0
        
        _min = max(prices)
        profit = 0
        for i in prices:
            if i < _min:
                _min = i
            else:
                profit = max(profit,i - _min)
        return profit
        
