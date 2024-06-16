class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        visited = [False] * len(nums)
        def backtracking(cnt, tmp):
            if n== cnt:
                ans.append(tmp.copy())
                return
            
            for i in range(0, n):
                if not visited[i]:
                    visited[i] = True
                    tmp.append(nums[i])
                    backtracking(cnt +1, tmp)
                    tmp.pop()
                    visited[i] = False

        backtracking(0,[])
        return ans