#include <iostream>

void func(void);        // 函数声明
static int count = 10;  // 全局变量，作用于整个文件内

extern void write_extern();  // 跨文件的函数或者变量，这个函数在storage_support.cpp中
int extern_variable;         // 同上

int main(int argc, char const *argv[])
{
    while(count--){
        func();
    }


    extern_variable = 10;       // 初始化，这个跨文件的变量
    write_extern();             // 调用别的文件的方法
    return 0;
}

void func(void)
{
    static int i = 5;       // 局部静态变量，但是离开函数时，不会销毁！！！
    i++;
    std::cout << "variable i = " << i;
    std::cout << ", variable count = " << count << std::endl;       // C++中::是引用相当于python和java中的.
}