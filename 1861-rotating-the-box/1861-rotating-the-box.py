class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        result = [["" for _ in range(m)] for _ in range(n)]

        # Create the transpose of the input grid in `result`
        for i in range(n):
            for j in range(m):
                result[i][j] = box[j][i]

        # Reverse each row in the transpose grid to complete the 90° rotation
        for i in range(n):
            result[i].reverse()

        # Apply gravity to let stones fall to the lowest possible empty cell in each column
        for j in range(m):
            # Process each cell in column `j` from bottom to top
            for i in range(n - 1, -1, -1):
                if (
                    result[i][j] == "."
                ):  # Found an empty cell; check if a stone can fall into it
                    next_row_with_stone = -1

                    # Look for a stone directly above the empty cell `result[i][j]`
                    for k in range(i - 1, -1, -1):
                        if result[k][j] == "*":
                            break  # Obstacle blocks any stones above
                        if (
                            result[k][j] == "#"
                        ):  # Stone found with no obstacles in between
                            next_row_with_stone = k
                            break

                    # If a stone was found above, let it fall into the empty cell `result[i][j]`
                    if next_row_with_stone != -1:
                        result[next_row_with_stone][j] = "."
                        result[i][j] = "#"

        return result