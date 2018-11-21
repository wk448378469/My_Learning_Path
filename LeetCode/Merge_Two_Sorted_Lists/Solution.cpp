#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
 
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == NULL) return l2;
        if(l2 == NULL) return l1;
        ListNode head(0);
        ListNode* ptr = &head;
        while(l1 && l2){
            if (l1->val < l2->val){
                ptr->next = l1;
                l1 = l1->next;
            }else{
                ptr->next = l2;
                l2 = l2->next;
            }
            ptr = ptr->next;
        }
        ptr->next = l1 ? l1 : l2;
        return head.next;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    ListNode first(1);
    first.next = new ListNode(2);
    first.next->next = new ListNode(4);

    ListNode second(1);
    second.next = new ListNode(3);
    second.next->next = new ListNode(4);

    ListNode* result = s.mergeTwoLists(&first, &second);
    while(result){
        cout << result->val << endl;
        result = result->next;
    }
    return 0;
}