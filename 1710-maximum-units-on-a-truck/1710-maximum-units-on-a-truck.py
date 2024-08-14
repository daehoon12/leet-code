class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: (-x[1]))
        answer = 0

        for a, b in boxTypes:
            if truckSize - a < 0:
                answer += truckSize * b
                truckSize -= truckSize
                break
            truckSize -= a
            answer += a * b

        return answer
              