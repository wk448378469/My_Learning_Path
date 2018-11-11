#include <iostream>

using namespace std;

class Shape
{
    public:
        Shape(int a = 0, int b = 0)
        {
            width = a;
            height = b;
        }
        int area_usless()
        {
            cout << "this is parent class area: " << endl;
            return 0;
        }
        virtual int area_useful()   // 虚函数，其实很像是java里面的抽象方法的感觉，然后c++里也可以在基类里不实现细节的
        {
            cout << "this is parent class area: " << endl;
            return 0;
        }
    protected:
        int width;
        int height;
};

class Rectangle: public Shape
{
    public:
        Rectangle(int a = 0, int b = 0) : Shape(a,b){ }
        int area_usless()
        {
            cout << "Rectangle class area: " << endl;
            return width * height;
        }
        int area_useful()
        {
            cout << "Rectangle class area: " << endl;
            return width * height;
        }
};

class Triangle: public Shape
{
    public:
        Triangle(int a = 0, int b = 0) : Shape(a,b){ }
        int area_usless()
        {
            cout << "Triangle class area: " << endl;
            return width * height;
        }
        int area_useful()
        {
            cout << "Triangle class area: " << endl;
            return width * height;
        }
};

int main(int argc, char const *argv[])
{
    Shape *shape;
    Rectangle rec(10, 7);
    Triangle tri(19, 2);

    shape = &rec;
    rec.area_usless();      // 直接调用，其实调用了自己的方法
    rec.area_useful();      // 同上
    shape->area_usless();   // 但是利用指针的话，这个地方就用了父类的方法
    shape->area_useful();   // 加virtual后用指针来调用该方法，就掉用自己的了

    cout << "\n" << endl;

    shape = &tri;
    shape->area_usless();
    shape->area_useful();

    return 0;
}