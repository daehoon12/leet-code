class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        answer = []
        people.sort(key = lambda x: (-x[0], x[1]))
        for p in people:
            answer.insert(p[1], p)
        return answer