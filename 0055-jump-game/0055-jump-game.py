# 뛸 수 있는 step을 갱신해주면 어떨까?
# 현재 가리키고 있는 step의 값과 현재 뛸수 있는 step 값 중 큰 값을 계속 갱신하면 될듯..?

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        curr_step = nums[0]
        for idx,step in enumerate(nums):
            if idx == len(nums) -1:
                return True
                
            curr_step -= 1
            curr_step = max(curr_step, step)
            
            if curr_step <= 0:
                return False

        return True                
        