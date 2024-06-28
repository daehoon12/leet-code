import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left, answer = 0, sys.maxsize
        total = 0
        for right in range(n):
            total += nums[right]

            while total >= target:
                answer = min(answer, right - left + 1)
                total -= nums[left]
                left += 1
                
        return 0 if answer == sys.maxsize else answer

            

