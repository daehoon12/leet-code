class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[0] * n for _ in range(m)]
        for y in range(m):
            dp[y][0] = 1
            for x in range(1, n):
                if y != 0 :
                    dp[y][x] = dp[y-1][x] + dp[y][x-1]
                else:
                    dp[y][x] +=  dp[y][x-1]
        return dp[m-1][n-1]