class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = nums[0]

        for i in range(1, len(nums)):     
            curr -= 1
            if curr < 0:
                return False
            curr = max(curr, nums[i])

        return True
        
            