from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        score = defaultdict(int)
        players = set()
        answer = [[],[]]
        for winner, loser in matches:
            score[loser] += 1
            players.add(winner)
            players.add(loser)
        for player in players:
            if not score[player]:
                answer[0].append(player)
            elif score[player] ==1:
                answer[1].append(player)
        answer[0].sort()
        answer[1].sort()
        return answer
