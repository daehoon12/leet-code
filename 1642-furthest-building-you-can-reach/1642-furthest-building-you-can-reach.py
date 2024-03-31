import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        answer = 0
        heap = []
        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(heap, diff)
            if len(heap) > ladders:
                used_brick = heapq.heappop(heap)
                if bricks - used_brick < 0:
                    break
                bricks -= used_brick
            answer += 1
        return answer

                    