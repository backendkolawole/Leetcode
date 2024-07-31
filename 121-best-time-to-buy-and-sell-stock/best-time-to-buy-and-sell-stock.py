# declare a variable max_profit that will hold the max profit from buying and then seling stocks
# declare a variable k with initial value 0
# iterate through prices 
# if the price at current index is greater than the prices at index k
# calculate the profit
# update the max profit
# else update the pointer k to equal the index of current price


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        k = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[k]:
                profit = prices[i] - prices[k]
                max_profit = max(max_profit, profit)
            else:
                k = i
        
        return max_profit