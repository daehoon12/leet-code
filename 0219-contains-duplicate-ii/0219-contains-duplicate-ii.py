from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dic = defaultdict(int)
        for i in range(n):
            if nums[i] in dic and abs(dic[nums[i]] - i) <= k:
                return True
            dic[nums[i]] = i 
        
        return False