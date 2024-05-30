# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        points = []
        
        prev = None
        
        current = head
        i = 0
        while current and current.next:
            if prev:
                if ((prev.val < current.val and current.next.val < current.val) or
                    (prev.val > current.val and current.next.val > current.val)):
                    points.append(i)
            prev = current
            current = current.next
            i += 1
        if len(points) < 2:
            return [-1,-1]
        minDistance = float('inf')
        for a, b in zip(points, points[1:]):
            minDistance = min(b-a, minDistance)
        
            
        return [minDistance, points[-1]-points[0]]
                
            
        
        