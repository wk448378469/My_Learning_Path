#include <iostream>
#include <stack>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// 结构体和类的看成一个样子去操作就好
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> st1;
        stack<int> st2;
        ListNode* prev = NULL;
        ListNode* head;
        int sum = 0;
        
        while(l1) {
            st1.push(l1->val);
            l1 = l1->next;
        }
        
        while(l2) {
            st2.push(l2->val);
            l2 = l2->next;
        }
        
        while(!st1.empty() || !st2.empty()) {
            sum /= 10;
            if(!st1.empty()) {
                sum += st1.top();
                st1.pop();
            }
            
            if(!st2.empty()) {
                sum += st2.top();
                st2.pop();
            }
            
            head = new ListNode(sum % 10);
            head->next = prev;
            prev = head;
        }
        
        if(sum >= 10) {
            head = new ListNode(sum / 10);
            head ->next = prev;
        }
        return head;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    ListNode first(9);
    ListNode first2(3);
    first.next = &first2;
    ListNode second(3);

    ListNode* result = s.addTwoNumbers(&first, &second);
    cout << result->val << endl;
    result = result->next;
    cout << result->val << endl;

    return 0;
}