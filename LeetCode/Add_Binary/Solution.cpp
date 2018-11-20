#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        string s = "";
        
        int c = 0, i = a.size() - 1, j = b.size() - 1;
        while(i >= 0 || j >= 0 || c == 1)
        {
            c += i >= 0 ? a[i --] - '0' : 0;
            c += j >= 0 ? b[j --] - '0' : 0;
            s = char(c % 2 + '0') + s;
            c /= 2;
        }
        
        return s; 
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    string a = "101";
    string b = "101101";
    cout << s.addBinary(a,b) << endl;
    return 0;
}