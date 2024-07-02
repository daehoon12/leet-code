from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = Counter(nums)
        answer = 0
        if k == 0:
            for val in dic.values():
                if val > 1:
                    answer +=1
            return answer
        
        for i in dic.keys():
            if i + k in dic:
                answer += 1
        return answer

