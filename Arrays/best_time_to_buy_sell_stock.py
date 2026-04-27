"""
LeetCode 121 - Best Time to Buy and Sell Stock

Approach: Greedy

Idea:
- Track minimum price seen so far
- Calculate profit at each step
- Keep maximum profit

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices):
        # Step 1: Initialize
        min_price = float('inf')
        max_profit = 0

        # Step 2: Traverse prices
        for price in prices:

            # Update minimum price
            if price < min_price:
                min_price = price

            # Calculate profit
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        # Step 3: Return result
        return max_profit


# Driver Code
if __name__ == "__main__":
    prices = list(map(int, input("Enter prices: ").split()))
    sol = Solution()
    print("Maximum Profit:", sol.maxProfit(prices))
