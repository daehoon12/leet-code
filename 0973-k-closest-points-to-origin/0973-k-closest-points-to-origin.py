import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       
        def euclid_distance(x, y):
            return (x * x + y * y) ** (1/2)
        
        heap = []
        answer = []
        for x, y in points:
            heapq.heappush(heap, [euclid_distance(x, y), x, y])
        while k:
            element = heapq.heappop(heap)
            answer.append([element[1], element[2]])
            k -= 1
        return answer


