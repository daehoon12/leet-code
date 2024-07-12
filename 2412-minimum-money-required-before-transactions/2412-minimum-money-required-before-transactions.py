class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        ans = val = 0 
        for cost, cashback in transactions: 
            ans += max(0, cost - cashback)
            val = max(val, min(cost, cashback))
            print(ans, val)
        return ans + val 