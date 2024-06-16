class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer2 = []
        answer = []
        visited = [False] * len(nums)
        def dfs(cnt):
            if cnt == len(nums):
                answer2.append(copy.deepcopy(answer))
                return 

            for i in range(0, len(nums)):
                if not visited[i]:
                    visited[i] = True
                    answer.append(nums[i])
                    dfs(cnt+1)
                    answer.pop()
                    visited[i] = False
        dfs(0)
        return answer2
            
