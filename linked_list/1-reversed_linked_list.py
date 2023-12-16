# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        currentNode = head
        lastNode = None
        
        while currentNode is not None:
            itr_tracker = currentNode.next
            currentNode.next = lastNode
            lastNode = currentNode
            currentNode = itr_tracker
        return lastNode