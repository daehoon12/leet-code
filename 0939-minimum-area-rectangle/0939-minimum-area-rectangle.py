import sys
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        answer = sys.maxsize
        dots = set()
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(0, n):
                x2, y2 = points[j]
                if (x1, y2) in dots and (x2, y1) in dots:
                    answer= min(answer, abs(y2 - y1) * abs(x2 - x1))
            dots.add((x1, y1))

        return answer if answer != sys.maxsize else 0
