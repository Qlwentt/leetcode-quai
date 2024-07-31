from bisect import insort
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        prev = None
        total = 0
        neededTime.append(0)
        times = []
        for i, current in enumerate(colors + 'A'):
            if current == prev:
                heappush(times, neededTime[i])
            else:
                if prev != None:
                    while len(times) > 1:
                        total += heapq.heappop(times)
                times = [neededTime[i]]
            prev = current
        return total