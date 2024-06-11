# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leader = dummy
        follower = dummy
        
        while leader and n:
            leader = leader.next
            n -= 1
        
        while leader and leader.next:
            leader = leader.next
            follower = follower.next
        
        follower.next = follower.next.next
        return dummy.next