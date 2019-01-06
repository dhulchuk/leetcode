# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return str(self) == str(other)

    @staticmethod
    def from_list(l):
        first = ListNode(l[-1])
        r = first
        for x in l[:-1][::-1]:
            r.next = ListNode(x)
            r = r.next
        return first

    def __str__(self):
        a = self
        res = ''
        while a:
            res += str(a.val)
            a = a.next
        return res[::-1]


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre_first = p = ListNode(None)
        flag = 0
        while l1 or l2 or flag:
            if l1:
                value1 = l1.val
                l1 = l1.next
            else:
                value1 = 0
            if l2:
                value2 = l2.val
                l2 = l2.next
            else:
                value2 = 0
            flag, number = divmod(value1 + value2 + flag, 10)
            p.next = ListNode(number)
            p = p.next
        return pre_first.next


class Solution2:
    # using python built-in arithmetics
    def to_int(self, input_list):
        ll = input_list
        res = 0
        i = 0
        while ll:
            res += ll.val * 10 ** i
            ll = ll.next
            i += 1
        return res

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = self.to_int(l1)
        b = self.to_int(l2)
        first = res = ListNode(None)
        for x in str(a + b)[::-1]:
            res.next = ListNode(int(x))
            res = res.next
        return first.next


if __name__ == '__main__':
    assert str(ListNode.from_list([1, 2, 3])) == '123'
    a = ListNode.from_list([3, 4, 2])
    assert Solution2().to_int(a) == 342, Solution2().to_int(a)
    b = ListNode.from_list([4, 6, 5])
    expected = ListNode.from_list([8, 0, 7])
    r1 = Solution().addTwoNumbers(a, b)
    r2 = Solution2().addTwoNumbers(a, b)
    assert r1 == expected, str(r1)
    assert r2 == expected, str(r2)
    c = ListNode.from_list([4, 6, 5])
    d = ListNode.from_list([6, 6, 7])
    expected = ListNode.from_list([1, 1, 3, 2])
    r1 = Solution().addTwoNumbers(c, d)
    r2 = Solution2().addTwoNumbers(c, d)
    assert r1 == expected, str(r1)
    assert r2 == expected, str(r2)
