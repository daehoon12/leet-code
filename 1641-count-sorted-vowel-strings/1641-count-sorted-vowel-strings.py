class Solution:
    def countVowelStrings(self, n: int) -> int:
        answer = []
        volews = ['a','e','i','o','u']
        def backtracking(idx, ans):
            if len(ans) == n:
                answer.append("".join(ans))
                return
                
            for i in range(idx, 5):
                ans.append(volews[i])
                backtracking(i, ans)
                ans.pop()
        backtracking(0, [])
        return len(answer)
            