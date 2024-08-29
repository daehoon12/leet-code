class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = nums[0]
        n = len(nums)
        
        if n == 1:
            return True
            
        for i in range(n):
            steps -= 1

            if steps < 0:
                return False

            steps = max(steps, nums[i])
        
        return True
