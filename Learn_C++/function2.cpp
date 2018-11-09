#include <iostream>
using namespace std;

void swap(int *x, int *y);

int main(int argc, char const *argv[])
{
    int a = 100;
    int b = 200;

    cout << "before swap a = " << a << endl;
    cout << "before swap b = " << b << endl;

    // 指针调用
    swap(&a, &b);   // & 取地址运算符， 传入a和b的地址

    cout << "\nafter swap a = " << a << endl;
    cout << "after swap b = " << b << endl;    

    return 0;
}

void swap(int *x, int *y)
{
    int temp;
    temp = *x;      // * 寻地址运算符，找到地址x的变量值赋值给temp
    *x = *y;
    *y = temp;
    return;
}