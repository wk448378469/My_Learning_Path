class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
 
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode prev = head;
        while(true){
            if (l1 == null && l2 == null)
                break;
            if (l1 != null && l2 != null){
                if (l1.val > l2.val){
                    prev.next = new ListNode(l2.val);
                    l2 = l2.next;
                }
                else{
                    prev.next = new ListNode(l1.val);
                    l1 = l1.next;
                }
            }
            else if (l2 == null){
                prev.next = new ListNode(l1.val);
                l1 = l1.next;
            }
            else{
                prev.next = new ListNode(l2.val);
                l2 = l2.next;
            }
            prev = prev.next;
        }
        return head.next;
    }

    public static void main(String[] args) {
           Solution s = new Solution();
           ListNode first = new ListNode(1);
           first.next = new ListNode(2);
           first.next.next = new ListNode(4);

           ListNode second = new ListNode(1);
           second.next = new ListNode(3);
           second.next.next = new ListNode(4);

           ListNode result = s.mergeTwoLists(first, second);
           while(result != null){
                System.out.println(result.val);
                result = result.next;
           }
    }
}