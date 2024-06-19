from collections import defaultdict

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        answer = 0
        zeros = 0
        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1
            while zeros > 1:
                if (nums[left] == 0):
                    zeros -= 1
                left += 1
            
            answer = max(answer, right - left + 1 - zeros)
        return answer -1 if answer == len(nums) else answer
            
            


        