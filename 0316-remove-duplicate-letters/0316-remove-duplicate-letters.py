from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []

        for e in s:
            count[e] -= 1
            if e in stack:
                continue
                
            while stack and e < stack[-1] and count[stack[-1]] > 0:
                stack.pop()
            stack.append(e)
        return "".join(stack)