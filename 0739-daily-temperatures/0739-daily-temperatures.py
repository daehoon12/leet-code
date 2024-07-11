class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                poped_idx = stack.pop()
                answer[poped_idx] = idx - poped_idx 
            stack.append(idx)

        return answer