
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    #method1
    # pathA = []
    # tmpA = headA
    # while tmpA:
    #     pathA.append(tmpA.val)
    #     tmpA = tmpA.next
    # tmpB = headB
    # while tmpB:
    #     if tmpB.val in pathA:
    #         return tmpB
    #     tmpB = tmpB.next
    # return None
    #method2
    # tmpA = headA
    # while (tmpA):
    #     tmpB = headB
    #     while (tmpB):
    #         if tmpA == tmpB:
    #             return tmpA
    #         tmpB = tmpB.next
    #     tmpA = tmpA.next
    # return None
    #method3
    if headA==headB:
        return headA
    pa = headA
    pb = headB
    while pa!=pb:
        pa = headB if pa==None else pa.next
        pb = headA if pb==None else pb.next
    return pa