var maxProfit = function(prices) {
    let maxProfit = 0
    let i = 0
    let j = 1

    while (j < prices.length) {
        if (prices[j] > prices[i]) {
            profit = prices[j] - prices[i]
            maxProfit = Math.max(profit, maxProfit) 
        }
        else i = j
        j +=1
    }    
    return maxProfit
};