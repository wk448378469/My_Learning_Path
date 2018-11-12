#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> returnVector;
        unordered_map<int, int> mydict;

        for (int i = 0; i < nums.size(); ++i)
        {
            int another = target - nums[i];
            if (mydict.find(another) != mydict.end()) // get~
                {
                    returnVector.push_back(mydict[another]);
                    returnVector.push_back(i);
                    return returnVector;
                }
            mydict[nums[i]] = i;
        }

        returnVector.push_back(-1);
        returnVector.push_back(-1);
        return returnVector;
    }
};

int main(int argc, char const *argv[])
{
    Solution s = Solution();

    int a[4] = {2, 7, 11, 15};
    vector<int> nums(a, a+4);
    int target = 18;

    vector<int> result = s.twoSum(nums, target);
    cout << result[0] << "\t" << result[1] << endl;
    return 0;
}