class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        int ROWS = grid.length;
        int COLS = grid[0].length;
        for(int i=0;i<ROWS;i++){
            for(int j=0;j<COLS;j++){
                if(grid[i][j] == '1'){
                    count+=1;
                    dfs(i,j,ROWS,COLS,grid);
                }
            }
        }

        return count;
    }

    private static void dfs(int r, int c, int ROWS, int COLS, char[][] grid){
        if((r>=0 && r<ROWS) && (c>=0 && c<COLS) && grid[r][c] == '1'){
            grid[r][c] = '0';
            dfs(r,c+1,ROWS,COLS,grid);
            dfs(r,c-1,ROWS,COLS,grid);
            dfs(r+1,c,ROWS,COLS,grid);
            dfs(r-1,c,ROWS,COLS,grid);
        }
    }
}