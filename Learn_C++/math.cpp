// 导入一堆库
#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdlib>

// iostream中的std中的方法等可以直接使用，例如cout endl等
using namespace std;

int main(int argc, char const *argv[])
{
    cout << sin(2.32) << endl;
    cout << abs(-2.32) << endl;
    cout << log(2.32) << endl;
    cout << pow(2.32, 2) << endl;
    cout << sqrt(2.32) << endl;
    cout << floor(2.32) << endl;

    // 设置种子
    srand( (unsigned)time(NULL) );
    cout << "\n" << time(NULL) << "\n" << endl;

    for (int i = 0; i < 10; ++i)
    {
        cout << "random number: " << rand() << endl;
    }
    return 0;
}