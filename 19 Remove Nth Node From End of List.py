
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        p1 = head
        p2 = head
        for i in range(n):
            if p1.next is not None:
                p1 = p1.next
            else:
                return head.next
        
        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next
        return head
            