class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        maxLen = 0

        def check(start, end):
            nonlocal maxLen, left 

            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            
            if (end - start - 1) > maxLen:
                maxLen = (end - start - 1)
                left = start + 1
        
        if len(s) <= 1:
            return s

        for i in range(len(s)-1):
            check(i, i+1)
            check(i, i+2)
        return s[left:left + maxLen]
            
            