from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(y, x):
            q = deque()
            q.append((y,x))
            visited[y][x] = True
            
            while q:
                y, x = q.popleft()
                for i in range(4):
                    ny, nx = dy[i] + y, dx[i] + x
                    
                    if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and grid[ny][nx] == "1":
                        visited[ny][nx] = True
                        q.append((ny,nx))
                        

        n, m = len(grid), len(grid[0])
    
        dy, dx = [1,0,-1,0], [0,1,0,-1]
        visited = [[False] * m for _ in range(n)]
        answer = 0
        for y in range(n):
            for x in range(m):
                if not visited[y][x] and grid[y][x] == "1":
                    answer += 1
                    bfs(y,x)
        return answer                
        