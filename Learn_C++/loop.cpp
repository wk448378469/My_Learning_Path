#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int count = 10;

    while(count > 0)
    {
        cout << count << endl;
        count--;

        if (count == 5)
        {
            continue;
        }

        if (count == 3)
        {
            break;
        }
    }

    for (int i = 0; i < count; ++i)
    {
        printf("%d\n", i);
    }

    return 0;
}