# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == [] and list2 == []:
            return []
        else:
            dummyList_head = ListNode()
            dummyList_tail = dummyList_head
            
            while list1 is not None and list2 is not None:
                if list1.val < list2.val:
                    dummyList_tail.next = list1
                    list1 = list1.next
                else:
                    dummyList_tail.next = list2
                    list2 = list2.next
                dummyList_tail = dummyList_tail.next
            
            if list1 is not None:
                dummyList_tail.next = list1
            if list2 is not None:
                dummyList_tail.next = list2
        
            return dummyList_head.next          
            