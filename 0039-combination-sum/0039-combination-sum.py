class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer=[]
        def dfs(idx, element, summ):
            if summ == target:
                if sorted(element) not in answer:
                    answer.append(element)
            if summ > target:
                return
            
            for i in range(idx, len(candidates)):
                dfs(i, element+[candidates[i]], summ+candidates[i])
               
        candidates=sorted(candidates)
        dfs(0,[],0)
        return answer
        