#include <iostream>
using namespace std;

double balance[1];   // 声明时，需要确定长度(但是没什么用啊...)

int main(int argc, char const *argv[])
{
    int n[10];    // 定义

    //初始化
    for (int i = 0; i < 10; ++i)
    {
        n[i] = i + 100;
    }

    // 定义并初始化
    double balance[] = {1.0, 23.2, 3.1, 250.8, 1.1};

    for (int i = 0; i < 10; ++i)
    {
        printf("%d\n", n[i]);
        if (i < 5)
        {
            cout << balance[i] << endl;
        }
    }

    n[7] = 10000;
    cout << "new n[7] = " << n[7] << endl;

    return 0;
}