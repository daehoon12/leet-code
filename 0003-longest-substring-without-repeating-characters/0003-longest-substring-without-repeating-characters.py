from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        left = 0
        answer = 0
        for right, val in enumerate(s):
            if val in dic and dic[val] >= left:
                left = dic[val] + 1
            dic[val] = right
            answer = max(answer, right - left + 1)
        return answer
                
