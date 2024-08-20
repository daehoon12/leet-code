import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x):
            if parents[x] == x:
                return x
            parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            x = find(x)
            y = find(y)

            if x < y:
                parents[y] = x
            else:
                parents[x] = y

        n = len(points)
        edges = []
        
        # Build all edges with their weights (Manhattan distance)
        for i in range(n):
            for j in range(i + 1, n):
                weight = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                heapq.heappush(edges, (weight, i, j))
        
        parents = list(range(n))
        rank = [0] * n
        answer = 0
        edges_used = 0
        
        # Process the edges in order of smallest weight
        while edges and edges_used < n - 1:
            weight, u, v = heapq.heappop(edges)
            if find(u) != find(v):
                union(u, v)
                answer += weight
                edges_used += 1
        
        return answer
