class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        answer = 0
        n = total // cost1 
        for i in range(n+1):
            answer += (total - cost1 * i) // cost2 + 1
        return answer if answer else 1        