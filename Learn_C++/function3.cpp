#include <iostream>
using namespace std;

void swap(int &x, int &y);

int main(int argc, char const *argv[])
{
    int a = 100;
    int b = 200;

    cout << "before swap a = " << a << endl;
    cout << "before swap b = " << b << endl;

    // 引用调用
    swap(a, b);

    cout << "\nafter swap a = " << a << endl;
    cout << "after swap b = " << b << endl;    

    return 0;
}

void swap(int &x, int &y)
{
    int temp;
    temp = x;
    x = y;
    y = temp;
    return;
}