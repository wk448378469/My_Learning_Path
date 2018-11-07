#include <iostream>

using namespace std;

extern int a,b,c;       // 变量的声明，声明的作用在于让大家都能找到这个变量，而不用考虑上下顺序，目前来看是这样的
extern float f;
extern int func();      // 函数的声明，如果没有那函数的定义就要在使用的上面，否则就找不到了


int func()
{
    return 1024;
}

int main(int argc, char const *argv[])
{
    int a,b,c;          // 定义
    float f;


    a = 10;             // 初始化
    b = 20; 
    c = a + b;
    f = 70.0 / 3.0;

    cout << c << endl;
    cout << f << endl;
    cout << func() << endl;

    return 0;
}

