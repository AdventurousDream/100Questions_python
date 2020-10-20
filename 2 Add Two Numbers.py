import typing

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def readLinkedList(self, l : ListNode) -> int:
        resList = []
        while l.next is not None:
            resList.append(l.val)
            l = l.next
        resList.append(l.val)
        
        res = 0
        for val in resList[::-1]:
            res = res * 10 + val
        return res
    
    def createLinkedList(self, num : int) -> ListNode:
        resList = list(str(num))
        head = None
        for n in resList:
            head = ListNode(int(n),head)
        return head

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.createLinkedList(self.readLinkedList(l1) + self.readLinkedList(l2))


if __name__ == '__main__':
    solveObj = Solution()
    l1 = solveObj.createLinkedList(342)
    l2 = solveObj.createLinkedList(465)
    print(solveObj.addTwoNumbers(l1, l2))
    