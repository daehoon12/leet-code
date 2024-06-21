import sys
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        s = set()
        answer = sys.maxsize
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                x2, y2 = points[j]
                if (x2, y1) in s and (x1, y2) in s:
                    answer = min(answer, abs((y2 - y1) * (x2 - x1)))
            s.add((x1, y1))
        return 0 if answer == sys.maxsize else answer