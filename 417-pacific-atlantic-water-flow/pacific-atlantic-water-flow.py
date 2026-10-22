class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = ([1,0],[0,1], [-1,0], [0,-1])

        def dfs(r, c, visited, prevHeight):
            if r not in range(rows) or c not in range(cols) or heights[r][c] < prevHeight or (r,c) in visited:
                return
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr,nc,visited, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols-1])
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        
        return [[i,j] for (i, j) in pacific & atlantic]