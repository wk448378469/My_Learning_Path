#include <iostream>

using namespace std;

const int MAX = 5;

int main(int argc, char const *argv[])
{
    int var[MAX] = {999, 555, 472, 23, 442};        // 数组的地址是连续的
    int *ptr;
    ptr = var;        // 将指针指向数组的第一个元素！！

    for (int i = 0; i < MAX; ++i)
    {
        cout << ptr << "\t" << *ptr << endl;
        ptr++;          // 移动至下一个位置
    }

    cout << "\n" << endl;

    int *ptw;
    ptw = &var[MAX-1];  // 指针的值为最后一个元素的地址
    for (int i = MAX; i > 0; i--)
    {
        cout << ptw << "\t" << *ptw << endl;
        ptw--;
    }

    cout << "\n" << endl;

    ptr = var;
    while(ptr <= &var[MAX-1])   // 指针的值（地址，显示出来是32进制的）可以进行比较
    {
        // 利用指针来遍历数组
        cout << ptr << "\t" << *ptr << endl;
        ptr++;
    }

    return 0;
}