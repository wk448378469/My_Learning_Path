#include <iostream>
#include <unordered_set>
#include <string>

using namespace std;

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int res = 0;
        unordered_set<char> setJ(J.begin(), J.end());
        for (char s : S) 
        {
            if (setJ.count(s)) 
                res++;
        }
        return res;
    }
};

int main(int argc, char const *argv[])
{
    Solution s = Solution();
    string J = "aA";
    string S = "asdbosbdoabasABSUDUAS";

    int result = s.numJewelsInStones(J, S);
    cout << result << endl;

    return 0;
}