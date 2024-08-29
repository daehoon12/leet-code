class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key =lambda x: x[1])
        s,e = points[0]
        n = len(points)
        answer = 1
        for i in range(1, n):
            ns, ne = points[i]
            
            if ns > e:
                answer += 1
                e = ne    
                
        return answer
            