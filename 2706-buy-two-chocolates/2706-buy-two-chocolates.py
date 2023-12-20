class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        maxPrice, secondMaxPrice = math.inf, math.inf
        for i in range(len(prices)):
            if maxPrice > prices[i]:
                secondMaxPrice = maxPrice
                maxPrice = prices[i]
            elif secondMaxPrice > prices[i]:
                secondMaxPrice = prices[i]
        #print(maxPrice,secondMaxPrice)
        if maxPrice + secondMaxPrice <= money:
            return money - (maxPrice + secondMaxPrice)
        else:
            return money
        
#         prices.sort()
        
#         if prices[0] + prices[1] <= money:
#             return (money-prices[0]-prices[1])
#         else:
#             return money