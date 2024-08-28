class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = -10000000000
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            elif dp[i-1] < 0 and nums[i] > dp[i-1]:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i-1]

            answer = max(dp[i], answer)
        return answer
                
                