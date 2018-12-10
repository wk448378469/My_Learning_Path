#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty())
            return 0;

        int m = matrix.size();
        int n = matrix[0].size();
        int sz = 0, pre = 0;
        vector<int> dp(m+1, 0);
        for (int j = 0; j < n; ++j)
        {
            for (int i = 1; i <= m; ++i)
            {
                int temp = dp[i];
                if (matrix[i-1][j] == '1')
                {
                    dp[i] = min(dp[i], min(dp[i-1], pre)) + 1;
                    sz = max(sz, dp[i]);
                } else{
                    dp[i] = 0;
                }
                pre = temp;
            }
        }
        return sz * sz;
    }
};

int main(int argc, char const *argv[])
{
    vector<vector<char>> matrix =  {{'1','0','1','0','0'},{'1','0','1','1','1'},{'1','1','1','1','1'},{'1','0','0','1','0'}};
    Solution s;
    int result = s.maximalSquare(matrix);

    cout << result << endl;
    return 0;
}