from collections import defaultdict

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
                edges.append((i,j, w ))

        edges =sorted(edges, key=lambda x:(x[2], x[0]))
        parents = list(range(n))
        for edge in edges:
            if find(edge[0]) != find(edge[1]):
                union(edge[0], edge[1])
                answer += edge[2]

        return answer
