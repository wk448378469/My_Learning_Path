#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int *ptr = NULL;

    cout << ptr << endl;        // 指针的值（即指向的地址）
    cout << *ptr << endl;       // 这个地址也就是0的值，没有输出，因为这个地址表示的是不指向一个可访问的内存位置

    return 0;
}