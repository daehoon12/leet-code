class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key =lambda x: x[1])
        s,e = points[0]
        answer = 1
        for i in range(1, len(points)):
            ns, ne = points[i]
            if e < ns:
                answer +=1
                e = ne
            
        return answer