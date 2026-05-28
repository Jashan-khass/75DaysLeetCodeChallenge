from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    q = deque()
                    q.append((r, c))
                    grid[r][c] = "0"

                    while q:
                        x, y = q.popleft()

                        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                        for dx, dy in directions:
                            nx = x + dx
                            ny = y + dy

                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                                grid[nx][ny] = "0"
                                q.append((nx, ny))

        return islands


grid1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

obj = Solution()

print(obj.numIslands(grid1))
print(obj.numIslands(grid2))