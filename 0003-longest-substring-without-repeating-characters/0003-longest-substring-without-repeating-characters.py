from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if s_len == 0:
            return 0
        dic = defaultdict(int)
        left, right = 0, 0
        answer = 0
        
        while right < s_len:
            if not dic[s[right]]:
                dic[s[right]] += 1
                right += 1
            else:
                dic[s[left]] -= 1
                left += 1

            answer = max(right - left, answer)
        return answer
        

        