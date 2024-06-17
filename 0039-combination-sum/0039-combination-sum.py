class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = set()
        def dfs(total, tmp):
            if total >= target:
                if total == target:
                    answer.add(tuple(sorted(tmp)))
                return
                
            for i in range(0, len(candidates)):
                total += candidates[i]
                tmp.append(candidates[i])
                dfs(total, tmp)   
                tmp.pop()
                total -= candidates[i]
        dfs(0, [])
        return answer
        