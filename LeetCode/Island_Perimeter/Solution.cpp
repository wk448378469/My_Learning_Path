#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int m;
    int n;
    int perimeter;
    int islandPerimeter(vector<vector<int>>& grid) {
        perimeter = 0;
        m = grid.size();
        n = grid[0].size();

        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (grid[i][j] == 1)
                {
                    getCellPerimeter(i, j, grid);
                }
            }
        }
        return perimeter;
    }

private:
    void getCellPerimeter(int i, int j, vector<vector<int>>& grid){
        int cellPerimeter = 0;
        if ((i - 1 < 0) || (grid[i - 1][j] == 0))
            cellPerimeter++;
        if ((i + 1 == m) || (grid[i + 1][j] == 0))
            cellPerimeter++;
        if ((j - 1 < 0) || (grid[i][j - 1] == 0))
            cellPerimeter++;
        if ((j + 1 == n) || (grid[i][j + 1] == 0))
            cellPerimeter++;

        perimeter += cellPerimeter;
    }
};

int main(int argc, char const *argv[])
{
    Solution s = Solution();
    vector<vector<int>> grid = {{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}};
    int result = s.islandPerimeter(grid);
    cout << result << endl;
    return 0;
}