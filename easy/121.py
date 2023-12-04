# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        for right, right_price in enumerate(prices):
            if prices[left] > right_price:
                left = right
            elif profit < right_price - prices[left]:
                profit = right_price - prices[left]
        return profit