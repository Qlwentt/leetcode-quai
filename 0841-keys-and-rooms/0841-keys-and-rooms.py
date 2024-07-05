class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # rooms is an adj list
        visited = set()
        n = len(rooms)
        
        def dfs(room):
            visited.add(room)
            
            while rooms[room]:
                dfs(rooms[room].pop())
        
        dfs(0)
        return len(visited) == n