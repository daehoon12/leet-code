class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', ']': '[', '}': '{'}    
        for i in range(len(s)):
            if not dic.get(s[i]):
                stack.append(s[i])
            elif not stack or dic.get(s[i]) != stack[-1]:
                return False
            elif stack and dic.get(s[i]) == stack[-1]:
                stack.pop()
        return True if not stack else False