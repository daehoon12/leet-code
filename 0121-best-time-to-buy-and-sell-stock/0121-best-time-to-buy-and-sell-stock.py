class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        answer = 0
        for i in range(1, len(prices)):
            if prices[i] > curr:
                answer = max(answer, prices[i] - curr)
            else:
                curr = prices[i]
        return answer