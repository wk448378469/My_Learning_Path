class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        prev = head
        while(True):
            if not l1 and not l2:
                break
            if l1 is not None and l2 is not None:
                if l1.val > l2.val:
                    prev.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    prev.next = ListNode(l1.val)
                    l1 = l1.next
            elif l2 is None:
                prev.next = ListNode(l1.val)
                l1 = l1.next
            else:
                prev.next = ListNode(l2.val)
                l2 = l2.next
            prev = prev.next
        return head.next


if __name__ == '__main__':
    s = Solution()
    first = ListNode(1)
    first.next = ListNode(2)
    first.next.next = ListNode(4)

    second = ListNode(1)
    second.next = ListNode(3)
    second.next.next = ListNode(4)

    result = s.mergeTwoLists(first, second)
    while(result):
        print(result.val)
        result = result.next
