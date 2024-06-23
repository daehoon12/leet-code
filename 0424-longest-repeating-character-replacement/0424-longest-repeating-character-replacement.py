from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        left, answer = 0, 0
        for right, char in enumerate(s):
            count[char] += 1
            max_char_n = count.most_common()[0][1]
            
            if right - left + 1 - max_char_n > k:
                count[s[left]] -= 1
                left += 1
                
            answer = max(answer, right - left + 1)
                
        return answer
