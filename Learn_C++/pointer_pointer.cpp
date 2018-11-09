#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int var = 3000;         
    int *ptr = &var;        // 指向var的地址
    int **pptr = &ptr;      // 指向指针ptr的地址

    cout << var << "\t" << &var << endl;
    cout << ptr << "\t" << &ptr << "\t" << *ptr << endl;
    cout << pptr << "\t" << &pptr << "\t" << **pptr << endl;

    return 0;
}