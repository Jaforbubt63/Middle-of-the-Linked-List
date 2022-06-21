# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        if head.next is None:
            return head
        
        p1 = head
        p2 = head
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            
        return p1
        