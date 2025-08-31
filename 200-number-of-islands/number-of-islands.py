class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            # Base case: out of bounds or water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            # Mark current land as visited
            grid[r][c] = "0"
            # Explore all 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        # Traverse every cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1   # found a new island
                    dfs(r, c)    # mark whole island as visited

        return count
