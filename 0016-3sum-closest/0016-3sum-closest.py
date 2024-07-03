import sys

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        answer = sys.maxsize
        for i in range(n):
            a = nums[i]
            left, right = i+1, n-1

            while left < right:
                if abs(a + nums[left] + nums[right] - target)< abs(answer - target):
                    answer = a + nums[left] + nums[right]
                    
                if a + nums[left] + nums[right] <= target:
                    left += 1
                else:
                    right -= 1
                
                
        return answer
                