class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(i, j):
            nonlocal max_area
            area = 1
            stack = [(i, j)]
            stack.append((i,j))
            visited.add((i,j))
            directions = ([1,0], [0,1], [0,-1], [-1,0])
            while stack:
                x, y = stack.pop()
                for r, c in directions:
                    nr, nc = x + r, y + c
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        area += 1
                        stack.append((nr,nc))
            max_area = max(max_area, area)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i, j)


        

        return max_area



