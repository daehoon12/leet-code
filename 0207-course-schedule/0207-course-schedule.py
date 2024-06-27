from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
            
        traced =set()
        visited=set()
        
        def dfs(start):
            if start in traced:
                return False
            if start in visited:
                return True
          
            traced.add(start)
            for i in graph[start]:
                if not dfs(i):
                    return False
            traced.remove(start)
            visited.add(start)
            return True
        
        for i in list(graph):
            if not dfs(i):
                return False
            
        return True
                    