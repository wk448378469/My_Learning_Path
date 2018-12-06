#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int lo = 0;
        int hi = height.size() - 1;
        int maxArea = 0;
        int temp;
        while(lo < hi){
            temp = min(height[hi], height[lo]) * (hi - lo);
            if (temp > maxArea)
                maxArea = temp;
            if (height[hi] > height[lo])
                lo++;
            else
                hi--;
        }

        return maxArea;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> h = {2, 3, 10, 5, 7, 8, 9};
    int result = s.maxArea(h);
    cout << result << endl;
    return 0;
}