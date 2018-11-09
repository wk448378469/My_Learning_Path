#include <iostream>
using namespace std;

const int MAX = 3;

int main(int argc, char const *argv[])
{
    int var[MAX] = {322, 187, 536};
    int *ptr[MAX];                    // 指针数组，元素都是指向int变量的指针

    for (int i = 0; i < MAX; ++i)
    {
        ptr[i] = &var[i];   // 指针数组赋值
    }

    for (int i = 0; i < MAX; ++i)
    {
        cout << *ptr[i] << "\t" << ptr[i] << endl;
    }


    const char *names[MAX] = {"asdas", "wdwda", "qqq21"};

    for (int i = 0; i < MAX; ++i)
    {
        cout << names[i] << "\t" << &names[i] << "\t" << *names[i] << endl;
    }


    return 0;
}