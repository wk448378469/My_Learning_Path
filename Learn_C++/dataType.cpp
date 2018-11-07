#include <iostream>
#include <string>
#include <limits>

using namespace std;

enum color
{
    red,
    green=5,
    blue
};

int main()
{
    cout << "type: \t\t" << "*****************size*****************" << endl;
    cout << "bool: \t\t" << "sizeof: " << sizeof(bool) << endl;
    cout << "char: \t\t" << "sizeof: " << sizeof(char);
    cout << "\t max value: " << (numeric_limits<char>::max)();
    cout << "\t\t min value: " << (numeric_limits<char>::min)() << endl;

    cout << "int: \t\t" << "sizeof: " << sizeof(int);
    cout << "\t max value: " << (numeric_limits<int>::max)();
    cout << "\t\t min value: " << (numeric_limits<int>::min)() << endl;

    cout << "signed long: \t\t" << "sizeof: " << sizeof(signed long);
    cout << "\t\t max value: " << (numeric_limits<signed long>::max)();
    cout << "\t\t min value: " << (numeric_limits<signed long>::min)() << endl;

    cout << "short int: \t\t" << "sizeof: " << sizeof(short int);
    cout << "\t\t max value: " << (numeric_limits<short int>::max)();
    cout << "\t\t min value: " << (numeric_limits<short int>::min)() << endl;

    cout << "float: \t\t" << "sizeof: " << sizeof(float);
    cout << "\t\t max value: " << (numeric_limits<float>::max)();
    cout << "\t\t min value: " << (numeric_limits<float>::min)() << endl;

    cout << "unsigned short int: \t\t" << "sizeof: " << sizeof(unsigned short int);
    cout << "\t\t max value: " << (numeric_limits<unsigned short int>::max)();
    cout << "\t\t min value: " << (numeric_limits<unsigned short int>::min)() << endl;

    typedef int feet;
    feet newInttype = 1024;
    cout << "new int type value is: " << newInttype << endl;

    color c = blue;
    cout << "blue in enum is :" << c <<endl;

    return 0;
}