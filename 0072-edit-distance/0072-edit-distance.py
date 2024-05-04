class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_len, word2_len = len(word1), len(word2)
        dp = [[0] * (word2_len + 1) for _ in range(word1_len+1)]

        for i in range(1, word1_len + 1):
            dp[i][0] = i

        for i in range(1, word2_len + 1):
            dp[0][i] = i

        for i in range(1, word1_len + 1):
            for j in range(1, word2_len+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[word1_len][word2_len]