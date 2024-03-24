# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        tailL2 = list2
        while tailL2.next:
            tailL2 = tailL2.next
        
        break1 = None
        break2 = None
        curL1 = list1
        i = 0
        while curL1:
            if break1 is None and i+1 == a:
                break1 = curL1
            if break2 is None and i == b:
                break2 = curL1.next
            i += 1
            curL1 = curL1.next
        
        break1.next = list2
        tailL2.next = break2
        
        return list1
            
        