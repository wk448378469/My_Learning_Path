# include <iostream>
# include <cstring>
# include <string>

using namespace std;

int main(int argc, char const *argv[])
{
    // C风格的字符串，字符的数组
    char str1[11] = "Hello";
    char str2[11] = "World";
    char str3[11];

    int len;
    strcpy(str3, str1);     // 复制
    cout << str3 << endl;

    strcat(str1, str2);     // 合并
    cout << str1 << endl;

    len = strlen(str1);     // 求长度
    cout << len << endl;

    int cmp = strcmp(str1, str2);         // 字符串比较
    cout << cmp << endl;

    // C++风格的字符串，面向对象
    cout << "\r\n" << endl;
    string s1 = "Hello";
    string s2 = "World";
    string s3;
    int length;

    s3 = s1;                // 复制
    cout << s3 << endl;

    s3 = s1 + s2;               // 连接
    cout << s3 << endl;

    length = s3.size();
    cout << length << endl;


    return 0;
}