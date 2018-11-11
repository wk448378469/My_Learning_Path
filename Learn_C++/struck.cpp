#include <iostream>
#include <cstring>

using namespace std;

// 结构体，能存储一堆信息的方式，且可以存储不同类型的数据
struct Book
{
    char title[50];
    char author[50];
    int book_id;
};

void printBookUseVar(struct Book book);     // 结构体作为参数
void printBookUsePointer(struct Book *book);    // 结构体指针作为参数

int main(int argc, char const *argv[])
{
    Book book1;
    Book book2;

    strcpy(book1.title, "C++ Head First");  // 字符串复制
    strcpy(book1.author, "bob");
    book1.book_id = 12345;

    strcpy(book2.title, "Java Head First");
    strcpy(book2.author, "allen");
    book2.book_id = 22322;

    printBookUseVar(book1);
    printBookUsePointer(&book2);

    return 0;
}

void printBookUseVar(struct Book book)
{
    cout << book.title << endl;
    cout << book.author << endl;
    cout << book.book_id << endl;
}

void printBookUsePointer(struct Book *book)
{
    cout << book->title << endl;
    cout << book->author << endl;       // 如果指针向访问结构体里的变量，需要用到 -> 这个符号！！！注意下哈
    cout << book->book_id << endl;
}