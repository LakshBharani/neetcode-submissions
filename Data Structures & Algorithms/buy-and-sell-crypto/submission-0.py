class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        diff = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                diff = max(diff, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return diff
            