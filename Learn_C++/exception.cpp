#include <iostream>
#include <exception>

using namespace std;

struct MyException: public exception
{
    const char *what() const throw()
    {
        return "my c++ exception";
    }
};

int main(int argc, char const *argv[])
{
    try
    {
        throw MyException();
    }
    catch(MyException& e)
    {
        cout << "my exception catched" << endl;
        cout << e.what() << endl;
    }
    catch(exception& e)
    {
        cout << "other exception" << endl;
    }


    return 0;
}