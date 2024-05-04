class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for x in range(1, m):
            if obstacleGrid[0][x] == 0:
                dp[0][x] = dp[0][x-1]

        for y in range(1, n):
            if obstacleGrid[y][0] == 0:
                dp[y][0] = dp[y-1][0]
            for x in range(m):
                if obstacleGrid[y][x] == 0:    
                    dp[y][x] = dp[y-1][x] + dp[y][x-1]
        return dp[n-1][m-1]
        