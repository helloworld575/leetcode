# leetcode 206. Reverse Linked List

#由于之前做过完全相同的medium的题(见下一题），此次用一遍扫描算法解决


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        start = dummy.next
        then = start.next
        while then:
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        return head