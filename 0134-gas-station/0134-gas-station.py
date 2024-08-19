class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        answer = 0
        fuel = 0
        
        for idx, g in enumerate(gas):
            c = cost[idx]
            if fuel + g - c < 0:
                answer = idx + 1
                fuel = 0
            else:
                fuel += g - c
        return answer
            
        