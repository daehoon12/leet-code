class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for i in range(len(nums)):
            if i % 2 == 0:
                answer += nums[i]
        return answer