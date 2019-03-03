class ListNode(object):
    def __init__(self,a = 0,b = None):
        self.val = a
        self.next = b
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m-1):
            pre = pre.next

        start = pre.next
        then = start.next

        for i in range(n-m):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        return dummy.next

