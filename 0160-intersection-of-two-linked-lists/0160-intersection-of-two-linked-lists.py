# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        curA = headA
        curB = headB
        setA = set()
        
        while curA:
            setA.add(curA)
            curA = curA.next
        
        while curB:
            if curB in setA:
                return curB
            curB = curB.next
        
        return None