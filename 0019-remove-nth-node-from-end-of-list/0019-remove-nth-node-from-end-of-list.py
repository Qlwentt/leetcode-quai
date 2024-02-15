# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        numNodes = 0
        
        current = head
        
        while current:
            numNodes += 1
            current = current.next
            
        target = numNodes - n
        dummy = ListNode(0, head)
        current = dummy
        
        while target:
            target -= 1
            current = current.next
            
        current.next = current.next.next
        return dummy.next