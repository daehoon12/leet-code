import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) >= 2:
            first, second = -heapq.heappop(heap), -heapq.heappop(heap)
            heapq.heappush(heap, -(first - second))
        
        return -heap[0] if heap else 0

    
            
        