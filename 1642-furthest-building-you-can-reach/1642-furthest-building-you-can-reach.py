import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        answer = len(heights) -1
        for i in range(1, len(heights)):
            if heights[i] - heights[i-1] > 0:
                print(heights[i] - heights[i-1])
                heapq.heappush(heap, heights[i] - heights[i-1])
            
            if len(heap) > ladders:
                used = heapq.heappop(heap)
                if bricks - used < 0:
                    answer = i -1
                    break
                bricks -= used
                    
        return answer
            