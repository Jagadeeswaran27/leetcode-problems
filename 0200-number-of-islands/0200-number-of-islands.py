class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0

        def bfs(row,col):
            queue = deque([(row,col)])
            indices = [(0,1),(0,-1),(1,0),(-1,0)]
            while queue:
                r,c = queue.popleft()
                grid[r][c] == "0"
                for dr,dc in indices:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        grid[nr][nc] = "0"
        
        def dfs(row,col):
            if 0<=row<ROWS and 0<=col<COLS and grid[row][col] == "1":
                grid[row][col] = "0"
                dfs(row,col+1)
                dfs(row,col-1)
                dfs(row+1,col)
                dfs(row-1,col)
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count+=1
                    # bfs(r,c)
                    dfs(r,c)
        return count
        
