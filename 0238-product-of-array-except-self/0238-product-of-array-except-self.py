# 1 1 2 6
# 24 12 4 1

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        answer = [1] * len(nums)
        for i in range(len(nums)-1):
            mul *= nums[i]
            answer[i+1] = mul

        mul = 1    

        for i in range(len(nums)-1, 0, -1):
            mul *= nums[i]
            answer[i-1] = answer[i-1] * mul
        return answer