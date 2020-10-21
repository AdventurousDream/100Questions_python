from typing import List
import heapq
from queue import PriorityQueue as PQ

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n == 0:
            return None
        
        pq = PQ()
        for i,head in enumerate(lists):
            if head is not None:
                pq.put((head.val,i,head))

        dummy = ListNode()
        iterNext = dummy
        while True:
            if pq.empty():
                break

            val, i, head = pq.get()
            iterNext.next = ListNode(val)
            iterNext = iterNext.next
            
            if head.next is not None:
                pq.put((head.next.val, i, head.next))
        
        return dummy.next