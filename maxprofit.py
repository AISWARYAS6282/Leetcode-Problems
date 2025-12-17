class solution:
    def maxprofit(self,prices):
        min_price=float("inf") #because we want to find the minimum price including index 0 
        max_profit = 0 #becasue we start with no profit
        for price in prices:
            if price<min_price:
                min_price=price
            else:
                profit=price-min_price
                if profit>max_profit:
                    max_profit=profit
        return max_profit
if __name__ == "__main__":
    sol = solution()
    prices = [7,1,5,3,6,4]
    result = sol.maxprofit(prices)
    print(f"Maximum Profit: {result}")  # Output: 5
