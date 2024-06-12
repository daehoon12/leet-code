from collections import Counter, defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        seen = defaultdict(int)
        for e in s:
            count[e] -= 1
            if seen[e]:
                continue

            while stack and e < stack[-1] and count[stack[-1]] > 0:
                seen[stack.pop()] = False

            stack.append(e)
            seen[e] = True
        return "".join(stack)