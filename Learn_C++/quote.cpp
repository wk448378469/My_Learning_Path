#include <iostream>

using namespace std;

double vals[] = {10.1, 12.6, 123.2, 33.2};
double & setValues(int i)  // 这个函数返回一个引用
{
    return vals[i];  // 返回数组的i个元素的引用
}


int main(int argc, char const *argv[])
{
    int i;
    double d;

    i = 5;
    d = 11.8;

    // 定义并初始化引用（且是必须这么做，不可以像指针和变量那样，先定义，在赋值），
    int & r = i;            // r是一个初始化为i的整数引用
    double & s = d;

    // !!!!引用不可改!!!!
    // 应用不可以指向空地址，不像指针

    cout << r << endl;
    cout << &i << "\t" << &r << endl;
    cout << s << "\n" << endl;


    setValues(0) = 11.11;   // 因为函数返回的是引用，所以可以把函数放在赋值语句的左边
    setValues(1) = 22.22;
    setValues(2) = 33.33;
    setValues(3) = 44.44;
    for (int i = 0; i < 4; ++i)
    {
        cout << vals[i] <<endl;
    }

    return 0;
}