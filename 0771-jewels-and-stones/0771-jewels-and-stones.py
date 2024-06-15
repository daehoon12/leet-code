from collections import defaultdict, Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        jewels_dict = Counter(jewels)

        for stone in stones:
            if jewels_dict[stone]:
                answer += 1
        return answer