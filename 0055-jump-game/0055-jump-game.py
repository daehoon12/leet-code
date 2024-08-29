class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = nums[0]
        for idx, val in enumerate(nums):
            if idx == len(nums) -1:
                return True
            step = max(val, step)
            if step <= 0:
                return False
            step -= 1
            
        return True