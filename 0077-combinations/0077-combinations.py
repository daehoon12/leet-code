class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtracking(idx, tmp):
            if len(tmp) == k:
                ans.append(tmp.copy())
                return
            
            for i in range(idx, n+1):
                tmp.append(i)
                backtracking(i + 1, tmp)
                tmp.pop()
        backtracking(1, [])
        return ans
            