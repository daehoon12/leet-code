from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        answer = 0
        dic = defaultdict(int)
        total = 0
        dic[0] = -1
        for i, num in enumerate(nums):
            if num == 1:
                total += 1
            else:
                total -= 1

            if total in dic:
                answer = max(answer, i - dic[total])
            else:
                dic[total] = i        

        return answer

                