class Solution:
    UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[self.UNGUARDED] * n for _ in range(m)]

        # Mark guards' positions
        for row, col in guards:
            grid[row][col] = self.GUARD

        # Mark walls' positions
        for row, col in walls:
            grid[row][col] = self.WALL

        # Updates the visibility of a cell based on the current guard line state.
        def _updatecell_visibility(row, col, is_guard_line_active):
            # If current cell is a guard, reactivate the guard line
            if grid[row][col] == self.GUARD:
                return True

            # If current cell is a wall, deactivate the guard line
            if grid[row][col] == self.WALL:
                return False

            # If guard line is active, mark cell as guarded
            if is_guard_line_active:
                grid[row][col] = self.GUARDED
            return is_guard_line_active

        # Horizontal passes
        for row in range(m):
            is_guard_line_active = grid[row][0] == self.GUARD
            for col in range(1, n):
                is_guard_line_active = _updatecell_visibility(
                    row, col, is_guard_line_active
                )
            is_guard_line_active = grid[row][n - 1] == self.GUARD
            for col in range(n - 2, -1, -1):
                is_guard_line_active = _updatecell_visibility(
                    row, col, is_guard_line_active
                )

        # Vertical passes
        for col in range(n):
            is_guard_line_active = grid[0][col] == self.GUARD
            for row in range(1, m):
                is_guard_line_active = _updatecell_visibility(
                    row, col, is_guard_line_active
                )
            is_guard_line_active = grid[m - 1][col] == self.GUARD
            for row in range(m - 2, -1, -1):
                is_guard_line_active = _updatecell_visibility(
                    row, col, is_guard_line_active
                )

        # Count unguarded cells
        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == self.UNGUARDED:
                    count += 1
        return count