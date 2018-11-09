#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int * getRandom()
{
    static int r[10];       // 必须用static修饰，要不然不能返回局部变量的地址

    srand((unsigned)time(NULL));
    for (int i = 0; i < 10; ++i)
    {
        r[i] = rand();
        cout << r[i] << endl;
    }

    return r;
}

int main(int argc, char const *argv[])
{
    int *p;

    p = getRandom();

    for (int i = 0; i < 10; ++i)
    {
        cout << "~" << *(p + i) << endl;    // 用到了指针的算术运算
    }
    return 0;
}