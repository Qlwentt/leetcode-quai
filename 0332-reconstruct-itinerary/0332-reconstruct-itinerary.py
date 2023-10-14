
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for src, dst, in tickets:
            if src not in adj:
                adj[src] = []
            if dst not in adj:
                adj[dst] = []
            heapq.heappush(adj[src], (dst))

        topo = []

        def topsort(root, adj):
            if not root:
                return
            
            while adj[root]:
                nei = heapq.heappop(adj[root])
                topsort(nei, adj)

            topo.append(root)
            return

        topsort('JFK', adj)
        topo.reverse()
        return topo
  
