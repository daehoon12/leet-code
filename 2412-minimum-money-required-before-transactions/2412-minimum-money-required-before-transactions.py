class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # 거래로 인해 발생할 수 있는 모든 추가 비용을 모두 더하여 미리 계산
        total_negative_cash_flow = sum(max(0, cost - cashback) for cost, cashback in transactions)
        print(total_negative_cash_flow)
        # 시작 시점에 필요한 추가 금액을 0으로 초기화한다.
        max_additional_money_required = 0
      
        # 거래 비용이 환급액보다 큰 경우 (cost > cashback)
        # 필요한 최대 금액을 total_negative_cash_flow + cashback과 비교하여 갱신한다.
        # 이는 환급액을 고려하여 추가 비용을 계산하는 방식.

        # 거래 비용이 환급액보다 작거나 같은 경우 (cost <= cashback):
        # 필요한 최대 금액을 total_negative_cash_flow + cost와 비교하여 갱신한다.
        # 이는 거래 비용을 고려하여 추가 비용을 계산하는 방식.
        for cost, cashback in transactions:
            if cost > cashback:
                max_additional_money_required = max(max_additional_money_required, 
                                                    total_negative_cash_flow + cashback)
            else:
                max_additional_money_required = max(max_additional_money_required, 
                                                    total_negative_cash_flow + cost)
        return max_additional_money_required
