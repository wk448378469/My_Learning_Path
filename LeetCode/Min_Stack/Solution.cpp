#include <vector>
#include <iostream>

using namespace std;

class MinStack {
public:
    vector<int> a;
    vector<int> min;
    MinStack() {
        min.push_back(2147483647);
    }
    void push(int x) {
        a.push_back(x);
        if (x < min.back()) {
            min.push_back(x);
        } else {
            min.push_back(min.back());
        }
    }

    void pop() {
        a.pop_back();
        min.pop_back();
    }

    int top() {
        return a.back();
    }

    int getMin() {
        return min.back();
    }
};

int main(int argc, char const *argv[])
{
    MinStack s;
    s.push(-10);
    s.push(14);
    cout << s.getMin() << endl;
    cout << s.getMin() << endl;
    s.push(-20);
    cout << s.getMin() << endl;
    cout << s.getMin() << endl;
    cout << s.top() << endl;
    cout << s.getMin() << endl;
    s.pop();
    s.push(10);
    s.push(-7);
    cout << s.getMin() << endl;
    s.push(-7);
    s.pop();
    s.pop();
    cout << s.getMin() << endl;
    s.pop();
    return 0;
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */