from bisect import insort
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors = colors + 'Z'
        neededTime.append(0)
        stack = [["A", []]]
        time = 0
        for i, color in enumerate(colors):
            if color == stack[-1][0]:
                heapq.heappush(stack[-1][1],neededTime[i])
            else:
                while len(stack[-1][1]) > 1:
                    j = heapq.heappop(stack[-1][1])
                    time += j
                stack.append([color, [neededTime[i]]])
        
        return time