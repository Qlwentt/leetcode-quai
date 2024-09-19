class RecentCounter:

    def __init__(self):
        self.q = collections.deque([]) 
        

    def ping(self, t: int) -> int:
        self.q.append(t)
        lowerbound = t - 3000
        while self.q[0] < lowerbound:
            self.q.popleft()
        return len(self.q)
        

# Time O(3000 * N) = O(N) where N is number of calls to ping
# Space O(3000) = O(1)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)