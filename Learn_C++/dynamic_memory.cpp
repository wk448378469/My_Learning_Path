#include <iostream>
using namespace std;

class Box
{
    public:
        Box()
        {
            cout << "create a new box" << endl;
        }
        ~Box()
        {
            cout << "destroy a box" << endl;
        }
};

int main(int argc, char const *argv[])
{
    /*
        首先要理解new，为变量（指针）申请内存
        然后是理解delete，释放变量（指针）的内存

        然后是两个概念
            栈内存：函数内声明的所有变量都占用栈内存
            堆内存：程序中未使用的内存，在运行的时候可以动态分配的内存
    */
    Box *myBoxArray = new Box[4];       // 指针指向一个包含Box类的数组
    delete [] myBoxArray;
    cout << "array is gone" << endl;
    cout << &myBoxArray << endl;

    myBoxArray++;
    cout << &myBoxArray << endl;

    cout << "\n" << endl;

    int *a = NULL;
    if (!(a = new int))
    {
        cout << "memory out..." << endl;
        exit(-1);
    }else{
        cout << &a << endl;
    }

    int value = 1000;
    a = &value;     // 内存泄露，因为a已经分配了内存地址，你又给他指向别人的地址？

    // *a = value;  这样子比较好，给指针指向的地址一个存储值

    cout << &a << endl;
    cout << *a << endl;

    cout << &value << endl;


    return 0;
}