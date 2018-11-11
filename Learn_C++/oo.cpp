#include <iostream>
# include <string>

using namespace std;

class Box
{
    // 共有成员（属性+方法），就你懂得...
    public: 
        double length;
        double breadth;
        double height;
        static int objectCount;     // 静态成员，所有该类共享一个的那种

        // 声明
        void setLength(double length);
        void setBreadth(double breadth);
        void setHeight(double height);
        void setName(string name);
        string getName(void);
        string getType(void);
        friend void printNameAndType(Box box);     // 友元函数
        friend class truck;                      // 友元类，友元可以访问本类的private和protected成员

        // 声明并定义
        double getVolume(void)
        {   
            // 可以在内部定义方法
            return length * breadth * height;
        }

        Box(void)
        {    
            // 构造函数，也可以有参数的那种
            cout << "a new box was born~" << endl;
            objectCount++;
        }

        Box(const Box &obj)
        {
            // 这个函数叫做拷贝构造函数，用于赋值构造新对象，类作为参数传递给函数等情况时用到！
            cout << "use old box copy a new box~" << endl;
            objectCount++;
        }

        ~Box(void)
        {
            // 析构函数，就是创建的对象挂掉的时候调用
            cout << "a box is gone~" << endl;
            objectCount--;
        }

    // 私有成员，只有自己和“友元函数”可以访问
    private:
        string name;

    // 保护成员 ，子类可以访问的
    protected:
        string type = "Box";
};

int Box::objectCount = 0; // 静态成员的初始化，必须在类的外部定义。。。

void Box::setName(string name)
{
    // 也可以在外部定义方法
    this -> name = name;        // this指针，指向类自己的地址
}

string Box::getName(void)
{
    return this -> name;
}

string Box::getType(void)
{
    return type;
}

void Box::setLength(double length)
{
    this -> length = length;
}
void Box::setBreadth(double breadth)
{
    this -> breadth = breadth;
}
void Box::setHeight(double height)
{
    this -> height = height;
}

void printNameAndType(Box b)
{
    cout << b.name << "\t" << b.type << endl;
}


// 继承！！！
class smallBox : public Box
{
    /* 
        public 继承
        基类Box的
                public成员     在这里是   public
                private成员    在这里是   private    但是访问不到
                protected成员  在这里是   protected
    */
};
class meddleBox : protected Box
{
    /* 
        protected 继承
        基类Box的
                public成员     在这里是   protected
                private成员    在这里是   private      但是访问不到
                protected成员  在这里是   protected
    */
};

class bigBox : private Box
{
    /* 
        private 继承
        基类Box的
                public成员     在这里是   private
                private成员    在这里是   private
                protected成员  在这里是   private  但是访问不到
    */
};



int main(int argc, char const *argv[])
{
    Box box;
    box.setLength(1.0);
    box.setHeight(2.0);
    box.setHeight(3.0);

    string name = "my box";
    box.setName(name);

    cout << box.length << " * " << box.height << " * " << box.breadth << " = ";
    cout << box.getVolume() << endl;
    cout << box.getName() << endl;
    cout << box.getType() << endl;

    Box box2 = box;
    printNameAndType(box);

    Box *ptrBox;
    ptrBox = &box;  // 指向类的指针，就像指针指向结构体那个类似
    cout << ptrBox->length << "\t" << ptrBox->getName() << endl;

    cout << "current obj num = " << box.objectCount << endl;

    return 0;
}