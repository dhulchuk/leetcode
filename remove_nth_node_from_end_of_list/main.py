# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return str(self) == str(other)

    @staticmethod
    def from_list(l):
        first = ListNode(l[0])
        r = first
        for x in l[1:]:
            r.next = ListNode(x)
            r = r.next
        return first

    def __str__(self):
        a = self
        res = []
        while a:
            res.append(str(a.val))
            a = a.next
        return ''.join(res)


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ll = head
        size = 1
        while ll.next:
            ll = ll.next
            size += 1
        if size == n:
            return head.next
        ll = head
        for i in range(size - n - 1):
            ll = ll.next
        ll.next = ll.next.next
        return head


if __name__ == '__main__':
    ll1 = ListNode.from_list([1, 2, 3, 4, 5])
    res1 = Solution().removeNthFromEnd(ll1, 2)
    exp1 = ListNode.from_list([1, 2, 3, 5])
    assert res1 == exp1, res1

    ll2 = ListNode.from_list([1, 2])
    res2 = Solution().removeNthFromEnd(ll2, 1)
    exp2 = ListNode.from_list([1])
    assert res2 == exp2, res2

    ll3 = ListNode.from_list([1, 2])
    res3 = Solution().removeNthFromEnd(ll3, 2)
    exp3 = ListNode.from_list([2])
    assert res3 == exp3, res3

