class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = set()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                a = nums[i]
                b = nums[j]
                left = j + 1
                right = n -1

                while left < right:
                    if a + b + nums[left] + nums[right] == target:
                        answer.add((a,b,nums[left],nums[right]))
                        left += 1
                        right -= 1
                    elif a + b + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        return answer