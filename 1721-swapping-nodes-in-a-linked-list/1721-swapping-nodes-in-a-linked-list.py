# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # 1 -> 2 -> 3 -> 4 -> 5
        # L
        # F
        
        leader = head
        while k-1 and leader:
            leader = leader.next
            k -= 1
        
        first_node = leader
        
        follower = head
        while leader and leader.next:
            leader = leader.next
            follower = follower.next
        
        second_node = follower
        
        first_node.val, second_node.val = second_node.val, first_node.val
        return head
        
        