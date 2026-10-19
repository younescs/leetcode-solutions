class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = collections.deque()
            visited.add((r,c))
            directions = ([1,0], [-1, 0], [0,1], [0, -1])
            queue.append((r,c))
            while queue:
                row, col = queue.popleft()
                for coord1, coord2 in directions:
                    r,c = row + coord1, col + coord2
                    if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] =="1":
                        queue.append((r,c))
                        visited.add((r, c))
                   



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1
        
        return islands