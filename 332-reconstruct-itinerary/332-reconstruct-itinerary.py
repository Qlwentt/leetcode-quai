from collections import deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adjList = {src: collections.deque() for src, dest in tickets}
        
        for src , dest in tickets:
            adjList[src].append(dest)
            
        
        itinerary = ["JFK"]
        def visitInOrder(node):
            if len(itinerary) == len(tickets) + 1:
                return True
            if node not in adjList:
                return False

            temp = list(adjList[node])
            for neigh in temp:
                adjList[node].popleft()
                itinerary.append(neigh)
                if visitInOrder(neigh):
                    return itinerary
                adjList[node].append(neigh)
                itinerary.pop()
            return False
                
        visitInOrder("JFK")
        return itinerary
