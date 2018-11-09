#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int var1;
    char var2[20];

    cout << &var1 << endl;      // & 访问地址，在没有赋值的情况下
    cout << &var2 << endl;

    // 指针也是一个变量，有变量名，* 来强调这个变量名是个指针
    // 指针变量的值，就是某个变量的地址（即理解上的指向某个地址）
    
    // 指针的定义
    int     *ip;
    // 指针的赋值
    ip = &var1;

    var1 = 10;

    cout << ip << endl;

    // 利用指针查看变量的值
    cout << *ip << endl;        // * 寻址符



    return 0;
}