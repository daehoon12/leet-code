class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(mid):
            cnt = 0
            for p in piles:
                if p % mid == 0:
                   cnt += p // mid
                else:
                    cnt += p // mid + 1
            return cnt > h

        low, high = 1, sum(piles)
        
        while low < high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid
        return high

            