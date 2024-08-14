class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_price = prices[0]
        answer = 0
        for price in prices:
            if curr_price < price:
                answer += price - curr_price
            curr_price = price
        return answer