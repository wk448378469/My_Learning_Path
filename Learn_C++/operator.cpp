#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int a = 21;
    int b = 10;
    int c;

    c = a + b;
    cout << c << endl;
    c = a - b;
    cout << c << endl;
    c = a * b;
    cout << c << endl;
    c = a / b;
    cout << c << endl;
    c = a % b;
    cout << c + "\n" << endl;

    int d = 10;
    cout << d++ << endl;
    cout << d << endl;

    if (a >= b && a != b)
    {
        cout << "a >= b\n" << endl;
    }
    
    cout << "size of a is " << sizeof(a) << endl; // sizeof 是一个杂项运算符，返回变量的大小

    int x;
    x = a != b ? a : b;     // 三目运算符
    cout << x << endl;          

    int y;
    y = (a++), (a * b), (a + b);    // 逗号运算符，等于最后一个逗号后面的值
    cout << "y = " << y << endl;

    cout << "\ntransform float to int " << int(2.3232) << endl;     // 强制转换，这个和python像

    cout << &a << endl;         // &指针运算符，返回变量a的地址

    return d;
}