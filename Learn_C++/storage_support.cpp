#include <iostream>

extern int extern_variable;

void write_extern(void)
{
    std::cout << "extern_variable = " << extern_variable << std::endl;
}