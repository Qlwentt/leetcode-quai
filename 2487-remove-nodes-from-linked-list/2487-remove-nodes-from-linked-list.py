# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         5,2,13,3,8
#         8,3,13,2,5
        
#         8:8,3:8,13:13,2:13,5:13
        
#         0->5:13->2:13->13:13->3:8->8:8
#          ->2:13 
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        
        max_val = 0
        maxes = [0]* len(arr)
        # [8,8,13,13,13]
        for i in range(len(arr)-1,-1,-1):
            max_val = max(arr[i], max_val)
            maxes[i] = max_val
        
        
        dummy = ListNode(0, head)
        current = dummy
        i = 0
        while current and current.next:
            if current.next.val < maxes[i]:
                current.next = current.next.next
            else:
                current = current.next
            i += 1
        return dummy.next
            
                       
        