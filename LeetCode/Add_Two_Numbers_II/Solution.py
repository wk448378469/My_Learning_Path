# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0:
            return l2
        if l2.val == 0:
            return l1

        valueOne, valueTwo = 0, 0
        while(l1 is not None or l2 is not None):
            if l1 is not None:
                valueOne = valueOne*10 + l1.val
                l1 = l1.next
            if l2 is not None:
                valueTwo = valueTwo*10 + l2.val
                l2 = l2.next

        total = valueOne + valueTwo
        root = ListNode(0)
        while total:
            remainder, total = total % 10, total//10
            root.next, root.next.next = ListNode(remainder), root.next

        return root.next


if __name__ == '__main__':
    s = Solution()
    first = ListNode(9)
    first.next = ListNode(2)
    first.next.next = ListNode(3)

    second = ListNode(4)
    second.next = ListNode(5)

    result = s.addTwoNumbers(first, second)

    print(result.val*100 + result.next.val*10 + result.next.next.val)
