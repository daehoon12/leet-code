class Solution:
    def reverseParentheses(self, s: str) -> str:
        answer = []
        stack = []
        for idx, val in enumerate(s):
            if s[idx] == '(':
                stack.append(len(answer))
            elif s[idx] == ')':
                start_idx = stack.pop()
                answer[start_idx:] = answer[start_idx:][::-1]
            else:
                answer.append(val)
        return ''.join(answer)