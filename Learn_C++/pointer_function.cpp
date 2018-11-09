#include <iostream>
#include <ctime>

using namespace std;

// 函数声明
void getSeconds(unsigned long *par);    // 无符号的long型指针
double getAverage(int *arr, int size);  // 可以穿入数组也

int main(int argc, char const *argv[])
{
    unsigned long sec;
    getSeconds(&sec);          // 把sec这个变量的地址传入
    cout << sec << endl;


    int balance[5] = {123, 321, 222, 532, 1023};
    double avg;
    avg = getAverage(balance, 5);       // balance其实是数组的第一个元素的地址
    cout << avg << endl;

    return 0;
}

double getAverage(int *arr, int size)
{
    int i, sum = 0;
    double avg;

    for (i = 0; i < size; ++i)
    {
        sum += arr[i];
    }

    avg = double(sum) / size;
    return avg;
}

void getSeconds(unsigned long *par)
{
    *par = time(NULL);
    return;
}