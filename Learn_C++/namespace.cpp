#include <iostream>
using namespace std;

namespace first_space
{
    void func()
    {
        cout << "first_space" << endl;
    }
}

namespace second_space
{
    void func()
    {
        cout << "second_space" << endl;
    }

    // 命名空间的嵌套
    namespace third_space
    {
        void func()
        {
            cout << "third_space" << endl;
        }
    }
}

namespace first_space
{
    // 空间可以不连续
    void first_discontinue_func()
    {
        cout << "first_space_discontinue_func" << endl;
    }
}

int main(int argc, char const *argv[])
{
    using namespace first_space;
    func();

    second_space::func();

    func();

    second_space::third_space::func();

    first_discontinue_func();

    return 0;
}