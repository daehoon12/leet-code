class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)
        answer = set()
        for i in range(nums_len):
            left, right = i + 1, nums_len -1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    answer.add((nums[i], nums[left], nums[right]))
                    left +=1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0 :
                    right -= 1
                else:
                    left += 1
        return answer