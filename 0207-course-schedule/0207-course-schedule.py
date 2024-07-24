from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            visited.add(node)
            cycle.add(node)
            for next_node in graph[node]:
                if not dfs(next_node):
                    return False
            cycle.remove(node)
            return True

        graph = defaultdict(list)
        cycle = set()
        visited = set()
        for s,e in prerequisites:
            graph[e].append(s)
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        