from collections import defaultdict
import heapq, sys

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def djikstra(node):
            pq = []
            heapq.heappush(pq, (0, node))
            distances[node] = 0
            
            while pq:
                curr_w, curr_n = heapq.heappop(pq)
                if curr_w > distances[curr_n]:
                    continue
                
                for next_w, next_n in graph[curr_n]:
                    distance = curr_w + next_w
                    if distance < distances[next_n]:
                        distances[next_n] = distance
                        heapq.heappush(pq, (distance, next_n))
                        

        graph = defaultdict(list)
        distances = [sys.maxsize] * (n + 1)

        for s,e,w in times:
            graph[s].append((w,e))
        djikstra(k)
        for val in distances[1:]:
            if val == sys.maxsize:
                return -1
                
        return max(distances[1:])