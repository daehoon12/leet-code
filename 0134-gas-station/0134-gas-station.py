class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_info = [(i, g, c) for i, (g, c) in enumerate(zip(gas, cost))]
        gas_info.sort(key= lambda x: (x[2] - x[1]))
        answer = gas_info[0][0]
        tank = 0
        for i, g, c in gas_info:
            if tank - c + g < 0:
                return -1
            tank += (g - c)

        return answer
                

        