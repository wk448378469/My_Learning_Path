#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    /*
        常量的两种定义方法
            1、 const 类型 变量名 = 变量值;            有分号
            2、 #define 变量名 变量值                  无分号
    */

    const int INT1 = 212;
    const int INT2 = 215u;        // u-无符号
    const int INT3 = 0xFeeL;       // l-长整数

    cout << INT1 << endl;
    cout << INT2 << endl;
    cout << INT3 << endl;

    #define FLOAT1 3.134232
    #define FLOAT2 3134232E-6L     // 自己理解吧...
    cout << FLOAT1 << endl;
    cout << FLOAT2 << endl;

    const bool BOOL1 = true;
    const bool BOOL2 = false;
    const bool BOOL3 = 3.2;
    cout << BOOL1 << endl;
    cout << BOOL2 << endl;
    cout << BOOL3 << endl;

    const char CHAR1 = '\\';      // \为转移符号
    const char CHAR2 = '\t';
    cout << CHAR1 << CHAR2 << "Hello \n World~" << endl;

    return 0;
}