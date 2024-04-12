from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        dic = defaultdict(int)
        for idx, val in enumerate(nums):
            dic[val] = idx
        
        for idx, val in enumerate(nums):
            if target - val in dic and idx != dic[target-val]:
                return [idx,  dic[target-val]]
                
        return answer
                