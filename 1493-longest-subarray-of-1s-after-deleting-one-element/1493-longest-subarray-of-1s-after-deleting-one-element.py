class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(1) == len(nums):
            return len(nums)-1
        low, high = 0 ,0
        nums_len = len(nums)
        deleted = False
        answer, feasible = 0, 0
        while high < nums_len:
            if nums[high] == 1:
                feasible += 1
                high += 1
            elif nums[high] == 0 and not deleted:
                deleted = True
                high += 1
            elif nums[high] == 0 and deleted:
                if nums[low] == 0:
                    deleted = False
                elif nums[low] == 1:
                    feasible -= 1
                low += 1
            answer = max(answer, feasible)
        return answer