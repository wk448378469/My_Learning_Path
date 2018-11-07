#include <iostream>
using namespace std;

// 定义全局变量
int b;
// 定义全局变量并初始化
int c = 30;


int main(int argc, char const *argv[])
{
    // 定义局部变量并初始化，函数内有用
    int a = 10;

    // 全局变量初始化
    b = c - a;

    cout << a << endl;
    cout << b << endl;

    // 局部变量覆盖全局变量，仅在函数内有效
    int c = 60;
    cout << c << endl;

    return 0;
}