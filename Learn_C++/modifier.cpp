#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{

    unsigned x = 1; // 这个等于 unsigned int x;   int 隐含在其中了

    long double y = 1.2;
    short int i;
    short unsigned int j;
    
    j = 50000;      // 溢出了
    i = j;

    cout << i << "  " << j << "  " << y << endl;

    return x;
}