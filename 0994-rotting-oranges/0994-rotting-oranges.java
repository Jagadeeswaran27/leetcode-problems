class Solution {
    static class Pair{
        int row,col,time;

        Pair(int row, int col,int time){
            this.row = row;
            this.col = col;
            this.time = time;
        }
    }
    public int orangesRotting(int[][] grid) {
        int ROWS = grid.length;
        int COLS = grid[0].length;
        int freshCount = 0;

        Queue<Pair> q = new LinkedList<>();

        for(int i=0;i<ROWS;i++){
            for(int j=0;j<COLS;j++){
                if(grid[i][j] == 1){
                    freshCount++;
                }

                if(grid[i][j] == 2){
                    q.add(new Pair(i,j,0));
                }
            }
        }

        int[][] dirs = {{1,0},{0,1},{-1,0},{0,-1}};

        int time = 0;

        while(!q.isEmpty()){
            Pair pair = q.poll();

            int t = pair.time;
            int r = pair.row;
            int c = pair.col;

            time = Math.max(time,t);

            for(int d[]:dirs){
                int nr = r+d[0];
                int nc = c+d[1];

                if(nr>=0 && nc>=0 && nr<ROWS && nc<COLS && grid[nr][nc] == 1){
                    grid[nr][nc] = 2;
                    freshCount--;
                    q.add(new Pair(nr,nc,t+1));
                }
            }

        }

        if(freshCount>0) return -1;
        return time;
    }

}