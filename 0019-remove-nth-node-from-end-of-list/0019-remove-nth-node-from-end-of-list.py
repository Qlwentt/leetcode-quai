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
            
        numNodes = numNodes - (n+1)
        
        if numNodes < 0:
            head = head.next
            return head
            
        current = head
        while numNodes:
            numNodes -= 1
            current = current.next
            
        current.next = current.next.next
        return head