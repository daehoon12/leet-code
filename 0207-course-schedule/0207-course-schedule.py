from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(curr):
            if curr in traced:
                return False
            if curr in visited:
                return True

            traced.add(curr)
            for next_node in graph[curr]:                    
                if not dfs(next_node):
                    return False
            traced.remove(curr)
            visited.add(curr)
            return True

        graph = defaultdict(list)        
        visited = set()
        traced = set()
        for s,e in prerequisites:
            graph[e].append(s)

        for i in list(graph):
            if not dfs(i):
                return False 
        return True   

                

            
