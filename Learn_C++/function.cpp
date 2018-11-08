#include <iostream>
using namespace std;

int max(int num1, int num2 = 500);      //函数的声明，当前这种情况，默认参数要在声明时定义好

int main(int argc, char const *argv[])
{
    int a = 10;
    int b = 20;
    int c;
    int d;

    c = max(a, b);          // 传值调用，还有指针调用和引用调用
    printf("%d\n", c);

    d = max(a);
    printf("%d\n", d);

    // lambda，[外部变量调用，是传值还是应用要看符号的](参数) -> 返回类型 {函数体}(函数调用)
    int aa = [a](int x, int y) -> int {int z = x + y; return z + a;}(10, 10);

    printf("%d\n", aa);

    return 0;
}

int max(int num1, int num2)
{
    if (num1 > num2)
    {
        return num1;
    }
    else
    {
        return num2;
    }
}