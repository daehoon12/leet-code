class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        cnt = 0 
        for i, t in enumerate(temperatures):
            if not stack:
                stack.append([i, t])
            else:
                while stack and stack[-1][1] < t:
                    poped_idx = stack[-1][0]
                    answer[poped_idx] = i - poped_idx
                    stack.pop()
                stack.append([i, t])
        return answer
                    
                    