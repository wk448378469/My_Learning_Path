class Solution {
    public int islandPerimeter(int[][] grid) {
        int perimeter = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) perimeter += getCellPerimeter(i, j, grid);
            }
        }
        return perimeter;
    }

    public int getCellPerimeter(int i, int j, int[][] grid){
        int cellPerimeter = 0;
        if ((i - 1 < 0) || (grid[i - 1][j] == 0))
            cellPerimeter += 1;
        if ((i + 1 == grid.length) || (grid[i + 1][j] == 0))
            cellPerimeter += 1;
        if ((j - 1 < 0) || (grid[i][j - 1] == 0))
            cellPerimeter += 1;
        if ((j + 1 == grid[0].length) || (grid[i][j + 1] == 0))
            cellPerimeter += 1;

        return cellPerimeter;
    }

    public static void main(String[] args) {
        int[][] grid = {{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}};
        Solution s = new Solution();
        int result = s.islandPerimeter(grid);
        System.out.println(result);
    }
}