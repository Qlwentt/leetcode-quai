class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # [4,7,9]
        players.sort()
        heapq.heapify(trainers)
        # [2,5,8,8]
        count = 0
        for player in players:
            if trainers:
                while trainers and trainers[0] < player:
                    heapq.heappop(trainers)
                if not trainers:
                    break
                heapq.heappop(trainers)
                count += 1
        return count
                