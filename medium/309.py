# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cool_down, sell, hold = 0, 0, -inf

        for price in prices:
            prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold

            cool_down = max(prev_cool_down, prev_sell)
            sell = prev_hold + price
            hold = max(prev_hold, prev_cool_down - price)
            
        return max(sell, cool_down)