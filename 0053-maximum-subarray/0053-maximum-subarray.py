class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = -10000000000
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
            elif dp[i-1] < 0 and nums[i] > dp[i-1]:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i-1]
            answer = max(dp[i], answer)
        
        return answer


        

