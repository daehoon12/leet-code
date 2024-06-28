class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        low, high = 0,0
        n = len(nums)
        answer = n
        total = nums[low]
        while high < n:
            if total < target:
                high += 1
                if high == n:
                    break
                total += nums[high]
            elif total >= target:
                answer= min(answer, high - low + 1)
                total -= nums[low]
                low += 1
        return answer

            
        

