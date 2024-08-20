from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def union(x, y):
            x = find(x)
            y = find(y)

            if x < y:
                parents[y] = x
            else:
                parents[x] = y
        
        def find(x):
            if parents[x] == x:
                return x
            parents[x] = find(parents[x])
            return parents[x]

        n = len(points)
        edges = []
        answer = 0 
        for i in range(n):
            for j in range(i+1, n):
                w = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                heapq.heappush(edges, (w, i,j))

        parents = list(range(n))
          # Process the edges in order of smallest weight
        while edges:
            weight, u, v = heapq.heappop(edges)
            if find(u) != find(v):
                union(u, v)
                answer += weight
        return answer