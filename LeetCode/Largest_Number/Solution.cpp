#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        string ret;
        sort(nums.begin(),nums.end(),
            [](const int &m,const int&n){
                return to_string(m)+to_string(n)>to_string(n)+to_string(m);});
        for(int i=0;i<nums.size();++i){
            ret+=to_string(nums[i]);
        }
        if(ret[0]=='0')
            return "0";
        return ret;
    }
};


int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> v = {3,30,34,5,9};
    string result = s.largestNumber(v);
    cout << result << endl;
    return 0;
}