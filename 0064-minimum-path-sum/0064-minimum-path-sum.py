class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for x in range(m):
            if x != 0:
                grid[0][x] += grid[0][x-1]

        for y in range(1, n):
            for x in range(m):
                if x == 0:
                    grid[y][x] += grid[y-1][x]
                else:
                    grid[y][x] += min(grid[y][x-1], grid[y-1][x])
        
        return grid[n-1][m-1]