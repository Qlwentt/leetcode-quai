class Solution:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        def _is_valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        m, n = len(grid), len(grid[0])

        # Initialize distance matrix with infinity (large value)
        min_obstacles = [[float("inf")] * n for _ in range(m)]

        # Start from the top-left corner, accounting for its obstacle value
        min_obstacles[0][0] = grid[0][0]

        pq = [(min_obstacles[0][0], 0, 0)]  # (obstacles, row, col)

        while pq:
            obstacles, row, col = heapq.heappop(pq)

            # If we've reached the bottom-right corner, return the result
            if row == m - 1 and col == n - 1:
                return obstacles

            # Explore all four possible directions from the current cell
            for dr, dc in self.directions:
                new_row, new_col = row + dr, col + dc

                if _is_valid(new_row, new_col):
                    # Calculate the obstacles removed if moving to the new cell
                    new_obstacles = obstacles + grid[new_row][new_col]

                    # Update if we've found a path with fewer obstacles to the new cell
                    if new_obstacles < min_obstacles[new_row][new_col]:
                        min_obstacles[new_row][new_col] = new_obstacles
                        heapq.heappush(pq, (new_obstacles, new_row, new_col))

        return min_obstacles[m - 1][n - 1]      
            