#include <iostream>

using namespace std;

class Shape     // 基类1
{
    public:
        void setWidth(int w)
        {
            width = w;
        }
        void setHeight(int h)
        {
            height = h;
        }

    protected:
        int width;
        int height;
};

class PaintCost // 基类2
{
    public:
        int getCost(int area)
        {
            return area * 70;
        }
};

class Rectangle: public Shape, public PaintCost // 多继承
{
    // 之前见过了，继承分为public、private、protected三种，但貌似用的最多的就是public继承
    public: 
        int getArea()
        {
            return width * height;
        }

};

int main(int argc, char const *argv[])
{
    Rectangle rect;
    rect.setHeight(6);
    rect.setWidth(4);

    int area = rect.getArea();
    int cost = rect.getCost(area);

    cout << cost << endl;

    return 0;
}