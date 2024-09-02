from sortedcontainers import SortedSet
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        alive = SortedSet([i for i in range(n)])
        answer = []
        for start, end in queries:
            while True:
                last_alive_index = alive.bisect_right(start)
                if alive[last_alive_index] >= end:
                    break
                else:
                    alive.pop(last_alive_index)
            answer.append(len(alive)-1)

        return answer
            