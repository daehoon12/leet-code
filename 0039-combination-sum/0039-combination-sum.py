class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, path, target):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                # 현재 후보군을 포함한 새로운 경로와 갱신된 타겟 값으로 dfs 재귀 호출
                dfs(i, path + [candidates[i]], target - candidates[i])
        
        candidates.sort()  # 후보군 정렬
        result = []
        dfs(0, [], target)
        return result
