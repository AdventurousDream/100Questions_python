
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        head = dummy
        p1,p2 = l1,l2
        while p1 is not None or p2 is not None:
            if p1 is None:
                head.next = ListNode(p2.val)
                p2 = p2.next
            elif p2 is None:
                head.next = ListNode(p1.val)
                p1 = p1.next
            else:
                if p1.val <= p2.val:
                    head.next = ListNode(p1.val)
                    p1 = p1.next
                else:
                    head.next = ListNode(p2.val)
                    p2 = p2.next
            head = head.next
        return dummy.next