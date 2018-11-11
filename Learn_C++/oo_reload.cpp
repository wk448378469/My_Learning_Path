#include <iostream>

using namespace std;

class printData
{
    // 函数的重载，就是成员名一样，但是参数不同
    public:
        void print(int i)
        {
            cout << "int = " << i << endl;
        }

        void print(double f)
        {
            cout << "double = " << f << endl;
        }

        void print(char c[])
        {
            cout << "char [] = " << c << endl;
        }
};


class Line
{
    public:
        void setLength(double len)
        {
            length = len;
        }
        double getLength(void)
        {
            return length;
        }
        // 重载运算符+
        /* 有一些是不可以重载的，比如：
                            1 .
                            2 ->
                            3 ::
                            4 sizeof
                            5 ?:
                            6 #
        */  
        Line operator+(const Line& l)
        {
            Line line;
            line.length = this->length + l.length;
            return line;
        }
        // 重载++
        void operator++()
        {
            this->setLength(length + 1);
        }
    private:
        double length;

};


int main(int argc, char const *argv[])
{
    printData pd;

    pd.print(5);
    pd.print(50.233);
    char c[] = "hello";
    pd.print(c);

    Line l1, l2, l3;
    l1.setLength(10.1);
    l2.setLength(20.2);
    ++l2;
    l3 = l1 + l2;
    cout << l3.getLength() << endl;

    return 0;
}