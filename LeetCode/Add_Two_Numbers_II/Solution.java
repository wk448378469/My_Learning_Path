import java.util.Stack;

public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> valueOne = new Stack<Integer>();
        Stack<Integer> valueTwo = new Stack<Integer>();

        while(l1 != null || l2 != null){
            if (l1 != null) {
                valueOne.push(l1.val);
                l1 = l1.next;
            }
            if (l2 != null){
                valueTwo.push(l2.val);
                l2 = l2.next;
            }
        }

        ListNode result = new ListNode(0);
        int sum = 0;
        while(!valueOne.empty() || !valueTwo.empty()){
            if (!valueOne.empty()) sum += valueOne.pop();
            if (!valueTwo.empty()) sum += valueTwo.pop();
            result.val = sum % 10;
            ListNode head = new ListNode(sum / 10);
            head.next = result;
            result = head;
            sum /= 10;
        }

        return result.val == 0 ? result.next : result;
    }

    public static void main(String[] args) {

        Solution s = new Solution();
        ListNode first = new ListNode(7);
        first.next = new ListNode(2);
        first.next.next = new ListNode(6);
        first.next.next.next = new ListNode(3);

        ListNode second = new ListNode(1);

        ListNode result = s.addTwoNumbers(first, second);
        System.out.println(result.val*1000 + result.next.val*100 + result.next.next.val * 10 + result.next.next.next.val);
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}