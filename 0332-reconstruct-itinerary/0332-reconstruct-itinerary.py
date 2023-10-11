
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj, weights = {}, {}
        for src, dst, in tickets:
            if src not in adj:
                adj[src] = []
                weights[src] = self.calc_lex(src)
            if dst not in adj:
                adj[dst] = []
                weights[dst] = self.calc_lex(dst)
            heapq.heappush(adj[src], (weights[dst], dst))

        topo = []

        def topsort(root, adj):
            if not root:
                return
            
            while adj[root]:
                cost, nei = heapq.heappop(adj[root])
                topsort(nei, adj)

            topo.append(root)
            return

        topsort('JFK', adj)
        topo.reverse()
        return topo
    # weighted lexicographic cost (first char has most weight, second has second-most, etc.)
    def calc_lex(self, s):
        return sum([(ord(c) * ((3 - i)**((3 - i) + (3 - i)))) for i, c in enumerate(s)])
