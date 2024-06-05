class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        for i in range(len(nums)):
            low, high = i+1, len(nums)-1
            while low < high:
                if nums[i] + nums[low] + nums[high] == 0:
                    answer.add((nums[i], nums[low], nums[high]))
                    low += 1
                    high -= 1
                elif nums[i] + nums[low] + nums[high] > 0:
                    high -=1
                else:
                    low +=1
        return answer